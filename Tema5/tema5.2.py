'''
2. Mai adaugati un parametru functiei de la punctul anterior numit overwrite, cu o valoare default False
- daca overwrite este False functia va functiona exact cum e descris la punctul anterior
- daca overwrite este True atunci nota data ca parametru va inlocui toate celelalte note existente. Practic elevul va avea în
acest caz o singura nota în lista și anume nota data ca parametru
'''

catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10]
}


def adauga_nota(elev, nota, overwrite=False):
    if nota not in range(11):
        return 'Nota ' + str(nota) + ' este invalida!!'
    elif elev not in catalog:
        return 'Elevul ' + elev + ' nu este in aceasta clasa!!'
    elif overwrite:
        catalog[elev] = [nota]
        return ('Nota ' + str(nota) + ' a suprascris notele lui ' + elev)
    else:
        catalog[elev].append(nota)
        return ('Nota ' + str(nota) + ' a fost adaugata la notele lui ' + elev)


print(adauga_nota('Popescu Ion', 3, overwrite=True))    # suprascriu notele
print(adauga_nota('Ion Ion', 8))                        # elev inexistent
print(adauga_nota('Georgescu Gelu', 11))                # nota invalida
print(adauga_nota('Radulescu Ioana', 10))               # adaugare nota

print('\nCatalog actualizat:')
for k, v in catalog.items():
    print(k, v, sep=': ')
