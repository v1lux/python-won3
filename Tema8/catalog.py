def media(lista_note):
    """Functia media.
     
    Parameters
    ----------
    lista_note : list
        lista numerelor a caror medie o calculeaza functia

    Returns
    ----------
    float :
        returneaza media numerelor din lista data ca parametru
    """

    if len(lista_note) > 0:
        return round(sum(lista_note) / len(lista_note), 2)
    return 0


def citeste_catalogul(file_name):
    """Functia citeste_catalogul.

    Parameters
    ----------
    file_name : str
        numele fisierului pe care il citeste functia

    Returns
    ----------
    dict :
        returneaza catalogul ca dictionar
    """

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


def afiseaza_mediile(cat):
    """Functia afiseaza_mediile.

    Parameters
    ----------
    cat : dict
        dictionarul cu catalogul clasei

    Returns
    ----------
    None :
        afiseaza situatia mediilor
    """

    header = f"{'Elev':50}{'Media':>5}"
    sep = "-" * len(header)
    print(header)
    print(sep)
    for k, v in sorted(cat.items()):
        print(f"{k:50}{media(v):>5.2f}")


def scrie_situatia(cat: dict, output_file: str):
    """Functia scrie_situatia.

    Parameters
    ----------
    cat : dict
        dictionarul cu catalogul clasei
    output_file: str
        numele fisierului in care se scriu datele

    Returns
    ----------
    None :
        scrie numele, mediile si nr de note in fisierul dat ca parametru
    """

    with open(output_file, 'w') as f:
        header = f"{'Nume':25}{'Prenume':25}{'Medie':>5} {'Note':5}\n"
        sep = "-" * (len(header) - 2) + '\n'
        f.write(header)
        f.write(sep)
        for k, v in sorted(cat.items()):
            nume, prenume = k.split()
            f.write(f"{nume:25}{prenume:25}{media(v):>5.2f}{len(v):^5}\n")
        print(f"Situatia scolara a fost salvata in fisierul \"{output_file}\".")


def scrie_situatia_noua(clasa, output_file):
    """Functia scrie_situatia_noua.

        Parameters
        ----------
        clasa : list
            catalogul clasei - nume complet si medie
        output_file: str
            numele fisierului in care se scriu datele

        Returns
        ----------
        None :
            scrie numele si media finala in fisierul dat ca parametru
        """

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


def scrie_premiantii(cat, output_file):
    """Functia scrie_premiantii.

        Parameters
        ----------
        cat : dict
            dictionarul cu catalogul clasei
        output_file: str
            numele fisierului in care se scriu datele

        Returns
        ----------
        None :
            scrie premiantii in fisierul dat ca parametru
        """

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


def afla_media(file_name):
    """Functia afla_media.

        Parameters
        ----------
        file_name: str
            numele fisierului text din care citeste datele functia

        Returns
        ----------
        list :
            returneaza o lista cu nume si media
        """

    with open(file_name, "r") as f:
        out_list = []                               # lista pe care o voi returna
        in_list = f.readlines()                     # citesc fisierul rezultand o lista de stringuri
        for row in sorted(in_list):                 # parcurg lista de stringuri ordonata alfabetic
            nume = row.split(";")[0]                # extrag numele
            note_str = row.strip().split(";")[1:]   # extrag notele (lista de stringuri)
            note = [int(n) for n in note_str]       # convertesc notele (lista de intregi)
            out_list.append([nume, media(note)])
        return out_list


def afla_media_finala(l1, l2):
    """calculeaza si returneaza media finala"""
    """Functia afla_media_finala.

        Parameters
        ----------
        l1 : list
            lista cu nume si media
        l2: list
            lista cu nume si nota din teza

        Returns
        ----------
        list :
            calculeaza si returneaza media finala
        """

    situatia_finala = []
    for i in range(len(l1)):                                    # parcurg cele 2 liste cu medii si cu teze, care sunt deja ordonate alfabetic
        nume = l1[i][0]                                         # extrag numele din prima lista
        md = l1[i][1]
        teza = l2[i][1]
        situatia_finala.append([nume, media([md, teza])])       # calculez media finala dintre medie si teza
    return situatia_finala

