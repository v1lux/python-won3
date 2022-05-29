catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10]
}


def media(lista_note):
    if len(lista_note) > 0:
        return round(sum(lista_note) / len(lista_note), 2)
    return 0


def afiseaza_mediile():
    print(f"{'Elev':50}{'Medie':>5}")
    print("-" * 55)
    for k, v in catalog.items():
        print(f"{k:50}{media(v):>5.2f}")


afiseaza_mediile()
