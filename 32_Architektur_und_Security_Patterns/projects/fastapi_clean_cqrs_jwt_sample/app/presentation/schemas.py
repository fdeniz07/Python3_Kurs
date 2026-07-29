from pydantic import BaseModel


class LoginRequest(BaseModel):
    username: str


class RefreshRequest(BaseModel):
    refresh_token: str


class CreateCourseRequest(BaseModel):
    id: int
    title: str
