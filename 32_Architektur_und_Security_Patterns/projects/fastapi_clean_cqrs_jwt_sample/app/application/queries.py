from app.domain.errors import NotFoundError


class GetCourseQueryHandler:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, course_id: int):
        course = self.repository.get(course_id)
        if course is None:
            raise NotFoundError("course not found")
        return {"id": course.course_id, "title": course.title}


class ListCoursesQueryHandler:
    def __init__(self, repository):
        self.repository = repository

    def execute(self):
        return [{"id": c.course_id, "title": c.title} for c in self.repository.list_all()]
