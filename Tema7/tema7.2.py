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


def scrie_situatia(cat: dict, output_file: str):
    '''scrie numele, mediile si nr de note intr-un fisier'''
    with open(output_file, 'w') as f:
        header = f"{'Nume':25}{'Prenume':25}{'Medie':>5} {'Note':5}\n"
        sep = "-" * (len(header) - 2) + '\n'
        f.write(header)
        f.write(sep)
        for k, v in sorted(cat.items()):
            nume, prenume = k.split()
            f.write(f"{nume:25}{prenume:25}{media(v):>5.2f}{len(v):^5}\n")
        print(f"Situatia scolara a fost salvata in fisierul \"{output_file}\".")


catalog = citeste_catalogul('note.txt')
scrie_situatia(catalog, 'situatia_scolara.txt')
