d = {
    'Popescu Ion': (2, 5, 7),
    'Ionescu Geta': (10, 7, 9, 7),
    'Georgescu Gelu': (4, 2),
    'Radulescu Ioana': (5, 9, 6, 4, 10),
    'Ionescu Temistocle': (2, 9, 4, 10),
    'Popescu Electra': (2, 5, 3),
    'Bengescu Hortensia': (9,),
    'Popescu Sandokan': (7, 6, 7),
}

print("Nume de familie unice:")
print("-" * 22)
print('{:12} {:10}'.format('Nume', 'Frecventa'))
print("-" * 22)

nume = []
for item in d:
    nume.append(item.split()[0])  # fac o lista cu numele de familie

nume_unice = {}
for n in nume:
    nume_unice[n] = nume.count(n)  # creez un nou dictionar cu nume si frecventa

for nu in nume_unice:
    print('{:12}{:10}'.format(nu, nume_unice[nu]))

print("-" * 22)
