def durchschnittspreis(preise):
    if not preise:
        return None
    return sum(preise) / len(preise)
def produkt_filter(produkte, buchstabe):
    return list(filter(lambda produkt: produkt.startswith(buchstabe), produkte))
def max_preis(preise):
    if not preise:
        return None
    if len(preise) == 1:
        return preise[0]
    else:
        max_rest = max_preis(preise[1:])
        return preise[0] if preise[0] > max_rest else max_rest
def preis_mit_steuer(preis, steuersatz=19):
    return preis * (1 + steuersatz / 100)
def erhoehe_preise(preise, prozentsatz):
    return list(map(lambda preis: preis * (1 + prozentsatz / 100), preise))
def drucke_produktliste(produkte):
    for produkt in produkte:
        print(produkt)

# Beispielaufrufe:

preise = [10, 20, 30, 40]

produkte = ["Apfel", "Banane", "Zitrone", "Orange"]

erhoehung = 0.10  # 10%



print("Durchschnittspreis:", durchschnittspreis(preise))
print("Produkte mit 'B':", produkt_filter(produkte, 'B'))
print("Maximaler Preis:", max_preis(preise))
print("Preis mit Steuer:", preis_mit_steuer(100))
print("Preise erhöht:", erhoehe_preise(preise, erhoehung))
drucke_produktliste(produkte)
