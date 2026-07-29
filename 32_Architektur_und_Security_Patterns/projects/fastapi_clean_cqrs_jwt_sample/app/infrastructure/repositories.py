from app.domain.models import Course


class InMemoryCourseRepository:
    def __init__(self):
        self._items = {}

    def add(self, course: Course):
        self._items[course.course_id] = course

    def get(self, course_id: int):
        return self._items.get(course_id)

    def list_all(self):
        return list(self._items.values())
