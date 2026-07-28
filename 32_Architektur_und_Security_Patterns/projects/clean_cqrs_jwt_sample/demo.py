from auth import create_token_pair, verify_token
from cqrs import KursStore, KursCommandHandler, KursQueryHandler
from global_exception_handler import handle_exception


if __name__ == "__main__":
    store = KursStore()
    commands = KursCommandHandler(store)
    queries = KursQueryHandler(store)

    try:
        kurs_id = commands.create_kurs(1, "Clean Architecture in Python")
        print(queries.get_kurs(kurs_id))
        print(queries.get_kurs(99))
    except Exception as exc:
        print(handle_exception(exc))

    pair = create_token_pair("user-1")
    print("access_token_ok:", verify_token(pair["access_token"]))
    print("refresh_token_ok:", verify_token(pair["refresh_token"]))
