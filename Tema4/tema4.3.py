d = {
    'Popescu Ion': (2, 5, 7),
    'Ionescu Geta': (10, 7, 9, 7),
    'Georgescu Gelu': (4, 2),
    'Radulescu Ioana': (5, 9, 6, 4, 10),
    'Ionescu Temistocle': (2, 9, 4, 10),
    'Popescu Electra': (2, 5, 3),
    'Bengescu Hortensia': (3,),
    'Popescu Sandokan': (7, 6, 7),
}

print("-" * 32)
print('{:8} {:12} {:12}'.format('Medie', 'Nume', 'Prenume'))
print("-" * 32)

d2 = {}

for item in d:
    d2[sum(d[item]) / len(d[item])] = item  # dictionar nou cu key/values de la d inversate

for i in sorted(d2, reverse=True):  # sortez descrescator dupa cheie (media)
    print('{:0.2f}     {:12} {:12}'.format(i, d2[i].split()[0], d2[i].split()[1]))

print("-" * 32)