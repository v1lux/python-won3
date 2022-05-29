def media(lista_note: list) -> float:
    '''calculeaza media unei liste de numere'''
    if len(lista_note) > 0:
        return round(sum(lista_note) / len(lista_note), 2)
    return 0


def citeste_catalogul(file_name: str) -> dict:
    '''citeste un fisier text si returneaza catalogul ca dictionar'''
    with open(file_name, "r") as f:
        my_list = f.readlines()                             # citesc fisierul rezultand o lista de stringuri
        lista_elevilor = dict()                             # initializez un dictionar
        for elev in my_list:                                # parcurg lista de stringuri
            nume = elev.split(";")[0]                       # extrag primul element din fiecare string split-uit dupa ';' (nume prenume)
            note = elev.strip().split(";")[1:]              # extrag notele (lista de stringuri)
            lista_elevilor[nume] = [int(n) for n in note]   # populez dictionarul si convertesc notele din str in int
        return lista_elevilor


def scrie_premiantii(cat: dict, output_file: str):
    '''scrie premiantii intr-un fisier'''
    cat2 = dict()
    for item in cat:
        cat2[media(cat[item])] = item                                               # dictionar nou cu keys = mediile
    with open(output_file, 'w') as f:
        header = f"{'Premiu':8}{'Nume':25}{'Prenume':25}{'Medie':>5}\n"
        sep = "-" * (len(header) - 1) + '\n'
        f.write(header)
        f.write(sep)
        premiul = 1
        for med, num in sorted(cat2.items(), reverse=True):                         # parcurg dictionarul sortat descrescator
            nume, prenume = num.split()
            if premiul <= 3:                                                        # scriu primii trei in ordinea mediilor
                f.write(f"{premiul:<8}{nume:25}{prenume:25}{med:>5.2f}\n")
                premiul += 1
        print(f"Situatia premiantilor a fost salvata in fisierul \"{output_file}\".")


catalog = citeste_catalogul('note.txt')
scrie_premiantii(catalog, 'lista_premianti.txt')
