"""
3. Pornind de la o cale existenta de pe unitatea voastra de stocare (de exemplu directorul unde aveti structura de fisiere Python)
parcurgeti cu os.walk() calea respectiva și afisati una sub alta toate fisierele python (care au extensia .py) precum și numarul lor
total. E posibil sa fie și fisiere python cu extensia .PY sau .Py. As vrea sa fie afisate indiferent de case-ul folosit. Exemplu de output:
C:/user/workspace/lab01/tema1.py
C:/user/workspace/lab02/modules/my_module.PY
C:/user/workspace/lab05/some-file.Py
Nr. python files: 3
"""

import os


def get_files_by_extension(path, ext):
    os.chdir(path)
    files_no = 0
    for root, folders, files in os.walk(path):
        for file in files:
            if file[-len(ext):].lower() == ext:
                print(os.path.join(root, file))
                files_no += 1
    if ext == ".py":
        return f"Python files: {files_no}"
    return f"{ext[1:]}-files: {files_no}"


start_dir = "/Users/vp/python_programs/python-won3/Tema11"
extension = ".txt"
print(get_files_by_extension(start_dir, extension))


