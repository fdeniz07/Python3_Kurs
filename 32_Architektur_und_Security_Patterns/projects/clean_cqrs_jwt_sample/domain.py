class AppError(Exception):
    pass


class NotFoundError(AppError):
    pass


class ValidationError(AppError):
    pass


class Kurs:
    def __init__(self, kurs_id, titel):
        self.kurs_id = kurs_id
        self.titel = titel
