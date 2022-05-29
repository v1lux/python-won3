import docx


def citeste_premiantii(file_name):
    """Functia citeste_premiantii.

    Parameters
    ----------
    file_name : str
        numele fisierului din care citeste functia

    Returns
    ----------
    dict :
        returneaza premiantii ca dictionar
    """

    with open(file_name, "r") as f:
        my_list = f.readlines()[2:]                                     # citesc fisierul incepand cu randul 3, rezultand o lista de stringuri
        lista_premiantilor = []                                         # initializez o lista
        for elev in my_list:                                            # parcurg lista de stringuri din fisier
            premiu, nume, prenume, medie = elev.split()
            lista_premiantilor.append([premiu, nume + ' ' + prenume, medie])   # populez lista cu valorile de care avem nevoie
        return lista_premiantilor                                       # returnez premiul, nume complet, media


def citeste_sablonul(file_name):
    """Functia citeste_sablonul.

    Parameters
    ----------
    file_name : str
        numele fisierului din care citeste functia

    Returns
    ----------
    dict :
        returneaza continutul fisierului
    """

    with open(file_name, "r") as f:
        my_list = f.read()
        return my_list


def scrie_diploma(file_name, locul):
    """Functia scrie_diploma.

        Parameters
        ----------
        file_name : str
            numele fisierului in care o sa scrie
        locul : int
            locul pe care il ocupa elevul in ordinea mediilor

        Returns
        ----------
        None :
            scrie valorile intr-un fisier txt
        """
    with open(file_name, "w") as f:
        a = citeste_premiantii('lista_premianti.txt')
        b = citeste_sablonul('diploma.txt')
        premiul = a[locul][0]
        #roman = lambda x: 'I' * int(x)                  # convertesc 1, 2, 3 in I, II, III
        nume_complet = a[locul][1]
        media = a[locul][2]
        f.write(b.format()(lambda x: 'I' * int(x)(premiul), nume_complet, media))


def scrie_diploma_docx(file_name, locul):
    """Functia scrie_diploma_docx.

        Parameters
        ----------
        file_name : str
            numele fisierului in care o sa scrie
        locul : int
            locul pe care il ocupa elevul in ordinea mediilor

        Returns
        ----------
        None :
            scrie valorile intr-un fisier docx
        """
    a = citeste_premiantii('lista_premianti.txt')
    b = citeste_sablonul('diploma.txt')
    premiul = a[locul][0]
    roman = lambda x: 'I' * int(x)                  # convertesc 1, 2, 3 in I, II, III
    nume_complet = a[locul][1]
    media = a[locul][2]
    my_docx = docx.Document()
    my_docx.add_paragraph(b.format(roman(premiul), nume_complet, media))
    my_docx.save(file_name)


for i in range(3):
    scrie_diploma(f'premiu-{i + 1}.txt', i)
    scrie_diploma_docx(f'premiu-{i + 1}.docx', i)


