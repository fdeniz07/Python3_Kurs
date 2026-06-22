print('Soll man heute draußen Sport treiben?')
antwort = input('Scheint die Sonne? (j/n): ')


if antwort == 'j':
    antwort = input('Hohe Luftfeuchtigkeit? (j/n): ')
    if antwort == 'j':
        print('Heute draußen keinen Sport treiben.')
    else:
        print('Ja, du kannst Sport treiben.')
else:
    antwort = input('Regnet es? (j/n): ')
    if antwort == 'j':
        antwort = input('Ist es windig? (j/n): ')
        if antwort == 'j':
            print('Heute draußen keinen Sport treiben.')
        else:
            print('Ja, du kannst Sport treiben.')
    else:
        print('Ja, du kannst Sport treiben.')
input("\nProgramm beendet. Enter drücken...")
