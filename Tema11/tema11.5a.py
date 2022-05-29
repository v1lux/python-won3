"""
5. a) La fel ca la problema 3, dar nu folosim os.walk() ci ne creem noi o functie recursiva care are un parametru string care va fi
folderul de start și care afiseaza fisierele .py din acel folder iar pentru subfoldere intra în recursivitate, afisand tot asa fisierele .py.
"""

import os


def johnny_walker(start_dir):
    for item in os.listdir(start_dir):
        if os.path.isdir(start_dir + "/" + item):
            johnny_walker(start_dir + "/" + item)
        elif item[-3:].lower() == ".py":
            print(start_dir + "/" + item)


path = '/Users/vp/python_programs/python-won3/Tema11'
johnny_walker(path)

