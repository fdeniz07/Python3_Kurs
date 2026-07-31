from domain.entities import Teilnehmer


class TeilnehmerService:
    def __init__(self, repository):
        self.repository = repository

    def teilnehmer_anlegen(self, id_, name, email):
        if "@" not in email:
            raise ValueError("ungueltige email")
        entity = Teilnehmer(id=id_, name=name.strip(), email=email.strip().lower())
        self.repository.save(entity)
        return entity
