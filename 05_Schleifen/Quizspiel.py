
# ---------------------------------------------
# Einfaches Quizspiel
# Autor: Fatih Deniz
# ---------------------------------------------

# Variable zum Zählen der richtigen Antworten
punkte = 0

# ---------------------------------------------
# Frage 1
# ---------------------------------------------
print("Frage 1:")
print("Welche Sprache wird häufig für Data Science verwendet?")
print("a) Python")
print("b) HTML")
print("c) CSS")

antwort = ""

while antwort not in ("a", "b", "c"):
    antwort = input("Ihre Antwort (a, b oder c): ")

    if antwort not in ("a", "b", "c"):
        print("Ungültige Eingabe! Bitte geben Sie a, b oder c ein.")

if antwort == "a":
    print("Richtig!")
    punkte += 1
elif antwort == "b":
    print("Falsch!")
else:
    print("Falsch!")


# ---------------------------------------------
# Frage 2
# ---------------------------------------------
print("\nFrage 2:")
print("Wie viele Kontinente gibt es auf der Erde?")
print("a) 5")
print("b) 7")
print("c) 9")

antwort = ""

while antwort not in ("a", "b", "c"):
    antwort = input("Ihre Antwort (a, b oder c): ")

    if antwort not in ("a", "b", "c"):
        print("Ungültige Eingabe! Bitte geben Sie a, b oder c ein.")

if antwort == "b":
    print("Richtig!")
    punkte += 1
elif antwort == "a":
    print("Falsch!")
else:
    print("Falsch!")


# ---------------------------------------------
# Frage 3
# ---------------------------------------------
print("\nFrage 3:")
print("Welche Zahl ist eine gerade Zahl?")
print("a) 7")
print("b) 11")
print("c) 8")

antwort = ""

while antwort not in ("a", "b", "c"):
    antwort = input("Ihre Antwort (a, b oder c): ")

    if antwort not in ("a", "b", "c"):
        print("Ungültige Eingabe! Bitte geben Sie a, b oder c ein.")

if antwort == "c":
    print("Richtig!")
    punkte += 1
elif antwort == "a":
    print("Falsch!")
else:
    print("Falsch!")


# ---------------------------------------------
# Auswertung
# ---------------------------------------------
print("\n===== Ergebnis =====")
print("Sie haben", punkte, "von 3 Fragen richtig beantwortet.")

if punkte == 3:
    print("Ausgezeichnet! Alle Antworten sind richtig.")
elif punkte >= 2:
    print("Gut gemacht!")
else:
    print("Sie können es noch einmal versuchen.")

