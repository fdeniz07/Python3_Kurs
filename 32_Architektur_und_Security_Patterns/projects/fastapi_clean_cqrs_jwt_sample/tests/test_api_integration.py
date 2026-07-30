import unittest

from fastapi.testclient import TestClient

from app.main import app


class TestApiIntegration(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_login_create_refresh_flow(self):
        login_res = self.client.post("/auth/login", json={"username": "alice"})
        self.assertEqual(login_res.status_code, 200)
        tokens = login_res.json()
        access = tokens["access_token"]
        refresh = tokens["refresh_token"]

        create_res = self.client.post(
            "/courses",
            headers={"Authorization": f"Bearer {access}"},
            json={"id": 1, "title": "DDD Basics"},
        )
        self.assertEqual(create_res.status_code, 200)

        refresh_res = self.client.post("/auth/refresh", json={"refresh_token": refresh})
        self.assertEqual(refresh_res.status_code, 200)

        reuse_res = self.client.post("/auth/refresh", json={"refresh_token": refresh})
        self.assertEqual(reuse_res.status_code, 401)

    def test_missing_bearer_returns_401(self):
        response = self.client.post("/courses", json={"id": 2, "title": "No Auth"})
        self.assertEqual(response.status_code, 401)


if __name__ == "__main__":
    unittest.main()
