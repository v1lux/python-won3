'''
1. Scrieti o functie care adauga o nota la un elev. Functia are doi parametri: elev și nota. Functia ii adauga la lista de note a
elevului nota data ca parametru. Functia trebuie sa verifice urmatoarele:
- nota data ca parametru sa fie intre 0 și 10, altfel sa dea mesaj de eroare și sa nu adauge nota
- elevul dat ca parametru sa existe în catalog, altfel sa dea mesaj de eroare
'''

catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10]
}


def adauga_nota(elev, nota):
    if nota not in range(11):
        return 'Nota ' + str(nota) + ' este invalida!!'
    elif elev not in catalog:
        return 'Elevul ' + elev + ' nu este in aceasta clasa!!'
    else:
        catalog[elev].append(nota)
        return ('Nota ' + str(nota) + ' a fost adaugata la notele lui ' + elev)


print(adauga_nota('Popescu Ion', 3))       # nume/nota valide
print(adauga_nota('Ion Ion', 7))           # elev inexistent
print(adauga_nota('Radulescu Ioana', 11))  # nota invalida

print('\nCatalog actualizat:')
for k, v in catalog.items():
    print(k, v, sep=': ')
