'''
4. Scrieti o functie care calculeaza media generala a clasei. Practic aceasta este media tuturor mediilor elevilor. Incercati sa
refolositi functia de calcul a mediei de data trecuta.
'''

catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10]
}


def media(lista_note):
    if len(lista_note) > 0:
        return round(sum(lista_note) / len(lista_note), 3)
    return 0


def media_clasei():
    lista_mediilor = []
    for elev in catalog:                                # parcurg dictionarul si fac o lista cu mediile fiecarui elev
        lista_mediilor.append(media(catalog[elev]))
    return str(media(lista_mediilor))                   # returnez media listei mediilor


print('Media generala este: ' + media_clasei())
