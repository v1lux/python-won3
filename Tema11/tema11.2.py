"""
2. Pornind de la o cale existenta de pe unitatea voastra de stocare (de exemplu C:/user/workspace) parcurgeti cu os.walk() calea
respectiva și contorizati toate fisierele și directoarele care se afla în structura arborescenta care porneste de la calea respectiva.
Programul va afisa doua numere: numarul total de fisiere și numarul total de directoare. Exemplu de output:
Path: C:/user/workspace
Nr. folders: 14
Nr. files: 53
"""


import os

a = "/Users/vp/python_programs/python-won3/Tema11"
folders_no = 0
files_no = 0
for root, folders, files in os.walk(a):
    for folder in folders:
        # print(os.path.join(root, folder))
        folders_no += 1
    for file in files:
        # print(os.path.join(root, file))
        files_no += 1

print(f"Path: {a}")
print(f"Nr. folders: {folders_no}")
print(f"Nr. files: {files_no}")

