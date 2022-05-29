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
    print(f"{'Nume':25}{'Prenume':25}{'Medie':>5} {'Note':5}")
    print("-" * 60)
    for k, v in catalog.items():
        print(f"{k.split()[0]:25}{k.split()[1]:25}{media(v):>5.2f}{len(v):^5}")


afiseaza_mediile()
