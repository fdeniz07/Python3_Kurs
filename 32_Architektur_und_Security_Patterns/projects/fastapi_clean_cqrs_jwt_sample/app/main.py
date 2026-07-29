from fastapi import FastAPI, Header

from app.application.commands import CreateCourseCommandHandler
from app.application.queries import GetCourseQueryHandler, ListCoursesQueryHandler
from app.domain.errors import AppError, AuthError, NotFoundError, ValidationError
from app.infrastructure.repositories import InMemoryCourseRepository
from app.presentation.schemas import CreateCourseRequest, LoginRequest, RefreshRequest
from app.security.token_service import TokenService
from app.security.token_store import SqliteTokenStore

app = FastAPI(title="Clean CQRS JWT Sample")

repository = InMemoryCourseRepository()
command_handler = CreateCourseCommandHandler(repository)
get_query = GetCourseQueryHandler(repository)
list_query = ListCoursesQueryHandler(repository)
token_store = SqliteTokenStore(db_path="./token_store.db")
token_service = TokenService(secret=b"very-secret-key", store=token_store)


def _extract_bearer(authorization: str | None) -> str:
    if not authorization or not authorization.lower().startswith("bearer "):
        raise AuthError("missing bearer token")
    return authorization.split(" ", 1)[1]


@app.exception_handler(ValidationError)
async def validation_exception_handler(_request, exc: ValidationError):
    return _json(400, str(exc))


@app.exception_handler(NotFoundError)
async def not_found_exception_handler(_request, exc: NotFoundError):
    return _json(404, str(exc))


@app.exception_handler(AuthError)
async def auth_exception_handler(_request, exc: AuthError):
    return _json(401, str(exc))


@app.exception_handler(AppError)
async def app_exception_handler(_request, exc: AppError):
    return _json(422, str(exc))


@app.exception_handler(Exception)
async def global_exception_handler(_request, _exc: Exception):
    return _json(500, "internal server error")


def _json(status: int, error: str):
    from fastapi.responses import JSONResponse

    return JSONResponse(status_code=status, content={"ok": False, "error": error})


@app.post("/auth/login")
def login(req: LoginRequest):
    pair = token_service.issue_pair(req.username.strip())
    return {"ok": True, **pair}


@app.post("/auth/refresh")
def refresh(req: RefreshRequest):
    pair = token_service.rotate_refresh(req.refresh_token)
    return {"ok": True, **pair}


@app.post("/auth/revoke")
def revoke(req: RefreshRequest):
    token_service.revoke_refresh(req.refresh_token)
    return {"ok": True}


@app.post("/auth/revoke-all/{user_id}")
def revoke_all(user_id: str):
    token_service.revoke_all_for_user(user_id)
    return {"ok": True}


@app.post("/courses")
def create_course(req: CreateCourseRequest, authorization: str | None = Header(default=None)):
    access_token = _extract_bearer(authorization)
    token_service.verify_access(access_token)
    course_id = command_handler.execute(req.id, req.title)
    return {"ok": True, "course_id": course_id}


@app.get("/courses/{course_id}")
def get_course(course_id: int):
    return {"ok": True, "data": get_query.execute(course_id)}


@app.get("/courses")
def list_courses():
    return {"ok": True, "data": list_query.execute()}
