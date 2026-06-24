# Initialisiere die Zählvariable für die richtigen Antworten

richtige_antworten = 0
# Frage 1

print("Frage 1: Was ist die Hauptstadt von Frankreich?")
print("a) Marseille\nb) Paris\nc) Lyon")
antwort = input("Deine Antwort (a, b, c): ")
while antwort not in ['a', 'b', 'c']:
    print("Ungültige Eingabe. Bitte wähle a, b, oder c.")
    antwort = input("Deine Antwort (a, b, c): ")
if antwort == 'b':
    richtige_antworten += 1
# Frage 2

print("Frage 2: Welcher Datentyp ist nicht veränderbar?")
print("a) Liste\nb) Tupel\nc) Wörterbuch")
antwort = input("Deine Antwort (a, b, c): ")
while antwort not in ['a', 'b', 'c']:
    print("Ungültige Eingabe. Bitte wähle a, b, oder c.")
    antwort = input("Deine Antwort (a, b, c): ")
if antwort == 'b':
    richtige_antworten += 1
# Frage 3

print("Frage 3: Welches Schlüsselwort wird in Python für eine unendliche Schleife verwendet?")
print("a) for\nb) while\nc) repeat")
antwort = input("Deine Antwort (a, b, c): ")
while antwort not in ['a', 'b', 'c']:
    print("Ungültige Eingabe. Bitte wähle a, b, oder c.")
    antwort = input("Deine Antwort (a, b, c): ")
if antwort == 'b':
    richtige_antworten += 1
# Gib die Anzahl der richtigen Antworten aus

print(f"Du hast {richtige_antworten} von 3 Fragen richtig beantwortet.")
# Rückmeldung basierend auf der Anzahl der richtigen Antworten

if richtige_antworten == 3:
    print("Ausgezeichnet! Du hast alle Fragen richtig beantwortet.")
elif richtige_antworten == 2:
    print("Gut gemacht! Du hast zwei Fragen richtig beantwortet.")
elif richtige_antworten == 1:
    print("Nicht schlecht! Du hast eine Frage richtig beantwortet.")
else:
    print("Schade! Vielleicht klappt es beim nächsten Mal besser.")
