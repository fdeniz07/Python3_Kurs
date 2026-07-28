import base64
import hashlib
import hmac
import json
import time

SECRET = b"demo-secret-key"


def _b64(data_bytes):
    return base64.urlsafe_b64encode(data_bytes).rstrip(b"=").decode("ascii")


def _sign(payload_text):
    return hmac.new(SECRET, payload_text.encode("utf-8"), hashlib.sha256).hexdigest()


def create_token(sub, expires_in_seconds):
    payload = {"sub": sub, "exp": int(time.time()) + expires_in_seconds}
    payload_text = json.dumps(payload, separators=(",", ":"), sort_keys=True)
    signature = _sign(payload_text)
    return _b64(payload_text.encode("utf-8")) + "." + signature


def verify_token(token):
    try:
        payload_b64, signature = token.split(".", 1)
        padded = payload_b64 + "=" * (-len(payload_b64) % 4)
        payload_text = base64.urlsafe_b64decode(padded.encode("ascii")).decode("utf-8")
        if not hmac.compare_digest(_sign(payload_text), signature):
            return {"ok": False, "fehler": "ungueltige signatur"}
        payload = json.loads(payload_text)
        if int(time.time()) > payload["exp"]:
            return {"ok": False, "fehler": "token abgelaufen"}
        return {"ok": True, "payload": payload}
    except Exception as fehler:
        return {"ok": False, "fehler": str(fehler)}


def create_token_pair(user_id):
    return {
        "access_token": create_token(user_id, 300),
        "refresh_token": create_token(user_id, 86400),
    }
