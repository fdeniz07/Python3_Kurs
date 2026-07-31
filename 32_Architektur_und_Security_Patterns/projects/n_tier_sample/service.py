from repository import KursRepository


class KursService:
    def __init__(self, repository=None):
        self.repository = repository or KursRepository()

    def kurse_laden(self):
        return self.repository.list_all()

    def kurs_detail(self, kurs_id):
        if kurs_id <= 0:
            raise ValueError("kurs_id muss positiv sein")
        kurs = self.repository.get_by_id(kurs_id)
        if kurs is None:
            raise LookupError("Kurs nicht gefunden")
        return kurs
