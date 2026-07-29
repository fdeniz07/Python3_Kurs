from app.domain.errors import ValidationError
from app.domain.models import Course


class CreateCourseCommandHandler:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, course_id: int, title: str):
        if course_id <= 0:
            raise ValidationError("course_id must be positive")
        if not title.strip():
            raise ValidationError("title must not be empty")
        course = Course(course_id=course_id, title=title.strip())
        self.repository.add(course)
        return course.course_id
