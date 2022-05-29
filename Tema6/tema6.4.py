def media(lista_note):
    if len(lista_note) > 0:
        return round(sum(lista_note) / len(lista_note), 2)
    return 0


def afiseaza_mediile():
    header = f"| {'Nume':20}{'Prenume':20}{'Medie':>5} {'Note':>5} |"
    sep = "-" * len(header)
    print(sep)
    print(header)

    print(sep)
    for k, v in catalog.items():
        nume, prenume = k.split()
        print(f"| {nume:20}{prenume:20}{media(v):>5.2f} {len(v):^5} |")
    print(sep)


catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10]
}

afiseaza_mediile()
