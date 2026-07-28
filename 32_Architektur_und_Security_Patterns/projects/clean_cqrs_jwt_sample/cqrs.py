from domain import Kurs, NotFoundError, ValidationError


class KursStore:
    def __init__(self):
        self._daten = {}


class KursCommandHandler:
    def __init__(self, store):
        self.store = store

    def create_kurs(self, kurs_id, titel):
        if not titel.strip():
            raise ValidationError("titel darf nicht leer sein")
        self.store._daten[kurs_id] = Kurs(kurs_id, titel)
        return kurs_id


class KursQueryHandler:
    def __init__(self, store):
        self.store = store

    def get_kurs(self, kurs_id):
        kurs = self.store._daten.get(kurs_id)
        if kurs is None:
            raise NotFoundError("kurs nicht gefunden")
        return {"id": kurs.kurs_id, "titel": kurs.titel}
