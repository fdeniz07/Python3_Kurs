from application.use_cases import TeilnehmerService
from infrastructure.in_memory_repo import InMemoryTeilnehmerRepository


if __name__ == "__main__":
    repo = InMemoryTeilnehmerRepository()
    service = TeilnehmerService(repo)
    print(service.teilnehmer_anlegen(1, "Ada", "ada@mail.de"))
    print(repo.all())
