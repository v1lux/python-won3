"""
5.b) La fel ca la problema 4, dar nu folosim os.walk() ci ne creem noi o functie recursiva care are un parametru string care va fi
folderul de start și care returneaza dimensiunea totala a fisierelor din acel folder (din tot arborele care porneste de la acel folder mai
exact)
"""

import os


def johnny_walker2(start_dir):
    file_size = 0
    for item in os.listdir(start_dir):
        if os.path.isdir(start_dir + "/" + item):
            johnny_walker2(start_dir + "/" + item)
        file_size += os.path.getsize(start_dir + "/" + item)
    return file_size


path = '/Users/vp/python_programs/python-won3/Tema11'
print(f"Start dir: {path} \nTotal file size: {johnny_walker2(path)}")
