# FastAPI Clean CQRS JWT Sample

Dieses Referenzprojekt zeigt:

- globale Exception-Handler in FastAPI
- CQRS (Command/Query Trennung)
- JWT-aehnliche Access/Refresh Token mit Rotation
- Refresh-Whitelist und Blacklist
- persistente Refresh-Token-Verwaltung ueber SQLite (`token_store.db`)

## Start

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Endpunkte

- `POST /auth/login`
- `POST /auth/refresh`
- `POST /auth/revoke`
- `POST /auth/revoke-all/{user_id}`
- `POST /courses` (mit Bearer Access Token)
- `GET /courses/{course_id}`
- `GET /courses`

## Tests

```bash
python -m unittest discover -s tests -p "test_*.py"
```
