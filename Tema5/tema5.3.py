'''
3. Scrieti o functie care sterge note, cu doi parametri elev și nota iar nota sa aiba o valoare default None.
- daca nota are o valoare diferita de None se va cauta nota în lista de note a elevului și daca exista se va sterge. Daca are
mai multe note de 7 de exemplu, se va sterge oricare, nu conteaza. Daca nu exista nota, se va afisa un mesaj de eroare
sugestiv.
- daca nota este None, vor disparea toate notele elevului și va avea o lista de note goala.
'''

catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10]
}


def sterge_nota(elev, nota=None):
    if not nota:
        catalog[elev].clear()       # daca nota e None, sterg toate notele acelui elev
        return 'Notele elevului ' + elev + ' au fost sterse.'
    elif nota not in catalog[elev]:
        return 'Nota inexistenta!!'  # daca nota e invalida sau nu exista printre notele acelui elev dau mesaj
    else:
        catalog[elev].remove(nota)
        return 'Nota ' + str(nota) + ' a elevului ' + elev + ' a fost stearsa din catalog.'


print(sterge_nota('Ionescu Geta', 12))      # nota invalida
print(sterge_nota('Georgescu Gelu'))        # nota=None, sterg toate notele
print(sterge_nota('Radulescu Ioana', 10))   # sterg nota

print('\nCatalog actualizat:')
for k, v in catalog.items():
    print(k, v, sep=': ')

