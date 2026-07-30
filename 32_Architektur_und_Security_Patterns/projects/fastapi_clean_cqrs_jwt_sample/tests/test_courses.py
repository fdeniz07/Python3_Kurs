import unittest

from app.application.commands import CreateCourseCommandHandler
from app.application.queries import GetCourseQueryHandler
from app.infrastructure.repositories import InMemoryCourseRepository


class TestCourseCQRS(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryCourseRepository()
        self.commands = CreateCourseCommandHandler(self.repo)
        self.queries = GetCourseQueryHandler(self.repo)

    def test_create_and_get(self):
        self.commands.execute(1, "Testkurs")
        result = self.queries.execute(1)
        self.assertEqual(result["id"], 1)
        self.assertEqual(result["title"], "Testkurs")


if __name__ == "__main__":
    unittest.main()
