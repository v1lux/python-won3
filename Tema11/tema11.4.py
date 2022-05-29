"""
4. Pe un server pe care il administram trebuie sa fim atenti la spatiul ocupat de un anumit director. Pentru asta trebuie sa scriem un
program care pornind de la acel director (cu os.walk()) contorizeaza dimensiunea totala a tuturor fisierelor din acel director. Va
trebui sa descoperiți care functionalitate din os sau alt modul (submodul din os) ne da dimensiunea unui fisier și apoi sa adunati
dimensiunile la un contor general. Exemplu de output:
Start dir: C:/user/Documents
Total file size: 12345678
"""

import os


def get_file_size(path):
    file_size = 0
    for root, folders, files in os.walk(path):
        for file in files:
            filename_with_path = os.path.join(root, file)
            file_size += os.path.getsize(filename_with_path)
    return file_size


start_dir = '/Users/vp/python_programs/python-won3'
print(f"Start dir: {start_dir} \nTotal file size: {get_file_size(start_dir)}")
