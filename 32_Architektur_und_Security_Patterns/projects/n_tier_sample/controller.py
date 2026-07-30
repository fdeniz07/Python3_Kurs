from service import KursService


def list_kurse():
    service = KursService()
    return {"ok": True, "daten": service.kurse_laden()}


def get_kurs(kurs_id):
    service = KursService()
    try:
        kurs = service.kurs_detail(kurs_id)
        return {"ok": True, "daten": kurs}
    except Exception as fehler:
        return {"ok": False, "fehler": str(fehler)}
