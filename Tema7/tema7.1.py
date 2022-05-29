def media(lista_note: list) -> float:
    """calculeaza media unei liste de numere"""
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
            #lista_elevilor[nume] = [int(n) for n in note]   # populez dictionarul si convertesc notele in lista de int
            lista_elevilor[nume] = []
            for n in note:
                lista_elevilor[nume].append(int(n))
        return lista_elevilor


def afiseaza_mediile(cat: dict):
    '''afiseaza elevii si media fiecaruia'''
    header = f"{'Elev':50}{'Media':>5}"
    sep = "-" * len(header)
    print(header)
    print(sep)
    for k, v in sorted(cat.items()):
        print(f"{k:50}{media(v):>5.2f}")


catalog = citeste_catalogul('note.txt')
afiseaza_mediile(catalog)
