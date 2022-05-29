'''
5. Scrieti o functie de calcul a mediei, care are doi parametri elev și materia. Materia are ca valoare default None.
- la apelul functiei, daca materia are vreuna dintre valorile m,r, sau f se va calcula media elevului la acea materie și se va
afisa un mesaj sugestiv de genul: Elevul X are media la matematica 7.55
- daca valoarea parametrului materia este None atunci se vor calcula mediile pentru fiecare materie și se va afisa mesajul:
Elevul X are urmatoarele medii:
matematica: 7.55
limba romana: 6.78
fizica: 5.60
'''

catalog = {
    'Popescu Ion': {
        'm': [2, 5, 7],
        'f': [],
        'r': [6, 9, 8],
    },
    'Ionescu Geta': {
        'r': [6, 3, 8],
        'm': [4, 5],
        'f': [7, 9, 10]
    },
    'Georgescu Gelu': {
        'm': [2, 5, 7, 9],
        'r': [9, 8],
        'f': [6, 9]
    },
    'Radulescu Ioana': {
        'm': [7],
        'f': [],
        'r': [6, 9, 8],
    },
}


def media(lista_note):
    if len(lista_note) > 0:
        return round(sum(lista_note) / len(lista_note), 2)
    return 0


def calculeaza_media(elev, materia=None):
    if elev not in catalog:
        return 'Elevul ' + elev + ' nu este in aceasta clasa!!'

    elif not materia:                                                               # materia=None
        return 'Elevul ' + elev + ' are urmatoarele medii:\n' \
               'matematica: ' + str(media(catalog[elev]['m'])) + ' \n' \
               'limba romana: ' + str(media(catalog[elev]['r'])) + ' \n' \
               'fizica: ' + str(media(catalog[elev]['f'])) + ' \n'

    elif materia in catalog[elev]:                                                  # verific daca materia e valida
        if materia == 'm':
            disciplina = 'matematica'
        elif materia == 'f':
            disciplina = 'fizica'
        else:
            disciplina = 'limba romana'
        return 'Elevul ' + elev + ' are media la ' + disciplina + ' ' + str(media(catalog[elev][materia]))

    else:
        return 'Materie inexistenta!!'


print(calculeaza_media('Radulescu Ioana'))      # materia=None
print(calculeaza_media('Georgescu Gelu', 'r'))  # calculez media la limba romana
print(calculeaza_media('Ion Ion'))              # nume inexistent
print(calculeaza_media('Ionescu Geta', 'x'))    # materie inexistenta