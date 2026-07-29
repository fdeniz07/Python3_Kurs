import base64
import hashlib
import hmac
import json
import secrets
import time

from app.domain.errors import AuthError
from app.security.token_store import SqliteTokenStore


class TokenService:
    def __init__(self, secret: bytes, store: SqliteTokenStore):
        self.secret = secret
        self.store = store

    def _b64(self, data_bytes: bytes) -> str:
        return base64.urlsafe_b64encode(data_bytes).rstrip(b"=").decode("ascii")

    def _unb64(self, value: str) -> bytes:
        padded = value + "=" * (-len(value) % 4)
        return base64.urlsafe_b64decode(padded.encode("ascii"))

    def _sign(self, payload_text: str) -> str:
        return hmac.new(self.secret, payload_text.encode("utf-8"), hashlib.sha256).hexdigest()

    def _encode(self, payload: dict) -> str:
        payload_text = json.dumps(payload, separators=(",", ":"), sort_keys=True)
        return self._b64(payload_text.encode("utf-8")) + "." + self._sign(payload_text)

    def _decode(self, token: str) -> dict:
        try:
            payload_b64, sig = token.split(".", 1)
            payload_text = self._unb64(payload_b64).decode("utf-8")
            expected = self._sign(payload_text)
            if not hmac.compare_digest(expected, sig):
                raise AuthError("invalid signature")
            payload = json.loads(payload_text)
            if int(time.time()) > int(payload["exp"]):
                raise AuthError("token expired")
            return payload
        except AuthError:
            raise
        except Exception as exc:
            raise AuthError(str(exc)) from exc

    def issue_pair(self, user_id: str) -> dict:
        now = int(time.time())
        access_payload = {
            "sub": user_id,
            "type": "access",
            "jti": secrets.token_hex(8),
            "exp": now + 300,
        }
        refresh_payload = {
            "sub": user_id,
            "type": "refresh",
            "jti": secrets.token_hex(16),
            "exp": now + 86400,
        }
        access = self._encode(access_payload)
        refresh = self._encode(refresh_payload)
        self.store.whitelist(refresh_payload["jti"], user_id)
        return {"access_token": access, "refresh_token": refresh}

    def verify_access(self, token: str) -> dict:
        payload = self._decode(token)
        if payload.get("type") != "access":
            raise AuthError("wrong token type")
        return payload

    def rotate_refresh(self, refresh_token: str) -> dict:
        payload = self._decode(refresh_token)
        if payload.get("type") != "refresh":
            raise AuthError("wrong token type")
        jti = payload.get("jti")
        if self.store.is_blacklisted(jti):
            raise AuthError("refresh token revoked")
        if not self.store.is_whitelisted(jti):
            raise AuthError("refresh token not whitelisted")

        self.store.blacklist(jti)
        return self.issue_pair(payload.get("sub", "unknown"))

    def revoke_refresh(self, refresh_token: str) -> None:
        payload = self._decode(refresh_token)
        if payload.get("type") != "refresh":
            raise AuthError("wrong token type")
        jti = payload.get("jti")
        self.store.blacklist(jti)

    def revoke_all_for_user(self, user_id: str) -> None:
        self.store.revoke_all_for_user(user_id)
