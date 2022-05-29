def media(lista_note: list) -> float:
    """calculeaza media unei liste de numere"""
    if len(lista_note) > 0:
        return round(sum(lista_note) / len(lista_note), 2)
    return 0


def citeste_catalogul(file_name: str) -> dict:
    """citeste un fisier text si returneaza catalogul ca dictionar"""
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
    """afiseaza elevii si media fiecaruia"""
    header = f"{'Elev':50}{'Media':>5}"
    sep = "-" * len(header)
    print(header)
    print(sep)
    for k, v in sorted(cat.items()):
        print(f"{k:50}{media(v):>5.2f}")


def scrie_situatia(cat: dict, output_file: str):
    """scrie numele, mediile si nr de note intr-un fisier"""
    with open(output_file, 'w') as f:
        header = f"{'Nume':25}{'Prenume':25}{'Medie':>5} {'Note':5}\n"
        sep = "-" * (len(header) - 2) + '\n'
        f.write(header)
        f.write(sep)
        for k, v in sorted(cat.items()):
            nume, prenume = k.split()
            f.write(f"{nume:25}{prenume:25}{media(v):>5.2f}{len(v):^5}\n")
        print(f"Situatia scolara a fost salvata in fisierul \"{output_file}\".")


def scrie_situatia_noua(clasa: list, output_file: str):
    """scrie numele si media finala intr-un fisier"""
    with open(output_file, 'w') as f:
        header = f"{'Nume':25}{'Prenume':25}{'Medie finala':>5}\n"
        sep = "-" * (len(header) - 1) + '\n'
        f.write(header)
        f.write(sep)
        for elev in clasa:
            nume, prenume = elev[0].split()
            media_finala = elev[1]
            f.write(f"{nume:25}{prenume:25}{media_finala:^12.2f}\n")
        print(f"Situatia scolara a fost salvata in fisierul \"{output_file}\".")


def scrie_premiantii(cat: dict, output_file: str):
    """scrie premiantii intr-un fisier"""
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


def afla_media(file_name: str) -> list:
    """citeste un fisier text si returneaza o lista cu nume si media"""
    with open(file_name, "r") as f:
        out_list = []                               # lista pe care o voi returna
        in_list = f.readlines()                     # citesc fisierul rezultand o lista de stringuri
        for row in sorted(in_list):                 # parcurg lista de stringuri ordonata alfabetic
            nume = row.split(";")[0]                # extrag numele
            note_str = row.strip().split(";")[1:]   # extrag notele (lista de stringuri)
            note = [int(n) for n in note_str]       # convertesc notele (lista de intregi)
            out_list.append([nume, media(note)])
        return out_list


def afla_media_finala(l1, l2: list) -> list:
    """calculeaza si returneaza media finala"""
    situatia_finala = []
    for i in range(len(l1)):                                    # parcurg cele 2 liste cu medii si cu teze, care sunt deja ordonate alfabetic
        nume = l1[i][0]                                         # extrag numele din prima lista
        md = l1[i][1]
        teza = l2[i][1]
        situatia_finala.append([nume, media([md, teza])])       # calculez media finala dintre medie si teza
    return situatia_finala

