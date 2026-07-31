class InMemoryTeilnehmerRepository:
    def __init__(self):
        self._daten = []

    def save(self, teilnehmer):
        self._daten.append(teilnehmer)

    def all(self):
        return list(self._daten)
