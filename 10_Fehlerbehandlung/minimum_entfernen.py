#----------------------------------------------------------------
# Dateiname: minimum_entfernen.py
# Test der Vorbedingungen in einer Funktion
#
#----------------------------------------------------------------
def entferne_min(s):
    'Entferne das Minimum in der Liste s.'
    assert type(s) == list  # s ist eine Liste
    assert len(s) > 0       # s enthält zumindest 1 Element
    m = min(s)
    s.remove(m)
    return s

if __name__ == '__main__':
    from random import shuffle
    s = list(range(10))
    shuffle(s)
    print(s)
    print(entferne_min(s))

    
