def media(lista_note):
    if len(lista_note) > 0:
        return round(sum(lista_note) / len(lista_note), 2)
    return 0


def lungime_max():
    max_nume = 4            # lungimea cuvantului 'Nume'
    max_prenume = 7         # lungimea cuvantului 'Prenume'
    for nume in catalog:                        # parcurg dictionarul si
        if max_nume < len(nume.split()[0]):     # returnez nr de litere pt cel mai lung nume si
            max_nume = len(nume.split()[0])     # pt cel mai lung prenume
        if max_prenume < len(nume.split()[1]):
            max_prenume = len(nume.split()[1])
    return max_nume, max_prenume    # returnez un tuple cu nr max de caractere pt nume si pt prenume


def afiseaza_mediile():
    print("-" * (lungime_max()[0] + lungime_max()[1] + 17))  # calculez nr de caractere total + extra spatii si |
    print(f"| {'Nume':{lungime_max()[0]}} {'Prenume':{lungime_max()[1]}} {'Medie':>5} {'Note':>5} |")
    print("-" * (lungime_max()[0] + lungime_max()[1] + 17))
    for k, v in catalog.items():
        print(f"| {k.split()[0]:{lungime_max()[0]}} {k.split()[1]:{lungime_max()[1]}} {media(v):>5.2f} {len(v):^5} |")
    print("-" * (lungime_max()[0] + lungime_max()[1] + 17))


catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10],
    'MirandaVelacruz DelahoyaCardinal': [5, 9, 6, 4, 9]
}


afiseaza_mediile()
