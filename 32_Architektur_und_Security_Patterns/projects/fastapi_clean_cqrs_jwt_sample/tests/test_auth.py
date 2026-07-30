import unittest
from pathlib import Path
from uuid import uuid4

from app.security.token_service import TokenService
from app.security.token_store import SqliteTokenStore


class TestTokenService(unittest.TestCase):
    def setUp(self):
        self.db_path = f"./tests/_token_test_{uuid4().hex}.db"
        self.store = SqliteTokenStore(db_path=self.db_path)
        self.service = TokenService(secret=b"test-secret", store=self.store)

    def tearDown(self):
        try:
            Path(self.db_path).unlink(missing_ok=True)
        except PermissionError:
            pass

    def test_issue_and_verify_access(self):
        pair = self.service.issue_pair("user-1")
        payload = self.service.verify_access(pair["access_token"])
        self.assertEqual(payload["sub"], "user-1")
        self.assertEqual(payload["type"], "access")

    def test_rotate_refresh(self):
        pair = self.service.issue_pair("user-2")
        rotated = self.service.rotate_refresh(pair["refresh_token"])
        self.assertIn("access_token", rotated)
        self.assertIn("refresh_token", rotated)

    def test_reuse_old_refresh_fails(self):
        pair = self.service.issue_pair("user-3")
        self.service.rotate_refresh(pair["refresh_token"])
        with self.assertRaises(Exception):
            self.service.rotate_refresh(pair["refresh_token"])


if __name__ == "__main__":
    unittest.main()
