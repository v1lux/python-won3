def media(lista_note: list) -> float:
    """calculeaza media unei liste de numere"""
    if len(lista_note) > 0:
        return round(sum(lista_note) / len(lista_note), 2)
    return 0


def afla_media(file_name: str) -> list:
    """citeste un fisier text si returneaza o lista cu nume si media"""
    with open(file_name, "r") as f:
        out_list = []                                       # lista pe care o voi returna
        in_list = f.readlines()                             # citesc fisierul rezultand o lista de stringuri
        for row in sorted(in_list):                         # parcurg lista de stringuri ordonata alfabetic
            nume = row.split(";")[0]                        # extrag numele
            note_str = row.strip().split(";")[1:]           # extrag notele (lista de stringuri)
            note = [int(n) for n in note_str]               # convertesc notele (lista de intregi)
            if len(note) > 3:                               # daca sunt mai mult de 3 note
                note = sorted(note, reverse=True)[:3]       # le iau pe primele 3 sortate descrescator
            out_list.append([nume, media(note)])
        #print(out_list)
        return out_list


def afla_media_finala(l1, l2: list) -> list:
    """calculeaza si returneaza media finala"""
    situatia_finala = []
    for i in range(len(l1)):                                    # parcurg cele 2 liste cu medii si cu teze, care sunt deja ordonate alfabetic
        nume = l1[i][0]                                         # extrag numele complet din prima lista
        md = l1[i][1]                                           # iau media din prima lista
        teza = l2[i][1]                                         # iau teza din a 2-a lista
        situatia_finala.append([nume, media([md, teza])])       # calculez media finala dintre medie si teza
    return situatia_finala


def afla_premiantii(lista: list, output_file: str):
    """calculeaza si scrie intr-un fisier premiantii"""
    premianti = []
    for elev in lista:
        premianti.append([elev[1], elev[0]])
    premianti = sorted(premianti, reverse=True)[:3]
    for elev in premianti:
        elev[0], elev[1] = elev[1], elev[0]
    scrie_situatia(premianti, output_file)


def afla_corigentii(lista: list, output_file: str):
    """calculeaza si scrie intr-un fisier corigentii"""
    corigenti = []
    for elev in lista:
        if elev[1] < 5:
            corigenti.append([elev[1], elev[0]])
    corigenti = sorted(corigenti, reverse=True)
    for elev in corigenti:
        elev[0], elev[1] = elev[1], elev[0]
    scrie_situatia(corigenti, output_file)



def scrie_situatia(clasa: list, output_file: str):
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


mediile = afla_media('note.txt')
note_teze = afla_media('teze.txt')                  # refolosesc 'afla media' pt a citi si fisierul cu notele din teze
situatia_finala = afla_media_finala(mediile, note_teze)

scrie_situatia(situatia_finala, 'noile_medii_finale.txt')
afla_premiantii(situatia_finala, 'premiantii.txt')
afla_corigentii(situatia_finala, 'corigentii.txt')



