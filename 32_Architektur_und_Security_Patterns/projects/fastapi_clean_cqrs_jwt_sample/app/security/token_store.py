import sqlite3
from pathlib import Path


class SqliteTokenStore:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._ensure_schema()

    def _connect(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _ensure_schema(self):
        Path(self.db_path).parent.mkdir(parents=True, exist_ok=True)
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS refresh_tokens (
                    jti TEXT PRIMARY KEY,
                    user_id TEXT NOT NULL,
                    status TEXT NOT NULL CHECK(status IN ('whitelisted','blacklisted'))
                )
                """
            )
            conn.commit()

    def whitelist(self, jti: str, user_id: str):
        self._ensure_schema()
        with self._connect() as conn:
            conn.execute(
                "INSERT OR REPLACE INTO refresh_tokens (jti, user_id, status) VALUES (?, ?, 'whitelisted')",
                (jti, user_id),
            )
            conn.commit()

    def blacklist(self, jti: str):
        self._ensure_schema()
        with self._connect() as conn:
            row = conn.execute("SELECT user_id FROM refresh_tokens WHERE jti = ?", (jti,)).fetchone()
            user_id = row["user_id"] if row else "unknown"
            conn.execute(
                "INSERT OR REPLACE INTO refresh_tokens (jti, user_id, status) VALUES (?, ?, 'blacklisted')",
                (jti, user_id),
            )
            conn.commit()

    def is_whitelisted(self, jti: str) -> bool:
        self._ensure_schema()
        with self._connect() as conn:
            row = conn.execute(
                "SELECT 1 FROM refresh_tokens WHERE jti = ? AND status = 'whitelisted'",
                (jti,),
            ).fetchone()
            return row is not None

    def is_blacklisted(self, jti: str) -> bool:
        self._ensure_schema()
        with self._connect() as conn:
            row = conn.execute(
                "SELECT 1 FROM refresh_tokens WHERE jti = ? AND status = 'blacklisted'",
                (jti,),
            ).fetchone()
            return row is not None

    def revoke_all_for_user(self, user_id: str):
        self._ensure_schema()
        with self._connect() as conn:
            conn.execute(
                "UPDATE refresh_tokens SET status = 'blacklisted' WHERE user_id = ?",
                (user_id,),
            )
            conn.commit()
