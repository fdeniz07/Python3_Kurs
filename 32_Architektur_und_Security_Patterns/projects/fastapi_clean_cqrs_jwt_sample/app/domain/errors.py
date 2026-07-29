class AppError(Exception):
    pass


class NotFoundError(AppError):
    pass


class ValidationError(AppError):
    pass


class AuthError(AppError):
    pass
