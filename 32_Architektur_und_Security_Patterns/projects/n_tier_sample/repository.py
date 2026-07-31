class KursRepository:
    def __init__(self):
        self._daten = [
            {"id": 1, "titel": "Python Grundlagen"},
            {"id": 2, "titel": "Architektur Patterns"},
        ]

    def list_all(self):
        return list(self._daten)

    def get_by_id(self, kurs_id):
        for kurs in self._daten:
            if kurs["id"] == kurs_id:
                return kurs
        return None
