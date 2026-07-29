from domain import AppError, NotFoundError, ValidationError


def handle_exception(exc):
    if isinstance(exc, ValidationError):
        return {"status": 400, "ok": False, "error": str(exc)}
    if isinstance(exc, NotFoundError):
        return {"status": 404, "ok": False, "error": str(exc)}
    if isinstance(exc, AppError):
        return {"status": 422, "ok": False, "error": str(exc)}
    return {"status": 500, "ok": False, "error": "internal server error"}
