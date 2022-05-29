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

print("Corigentii:")
print("-" * 32)
print('{:12} {:12}  {:8}'.format('Nume', 'Prenume', 'Medie'))
print("-" * 32)

c = {}

for item in d:
    media = sum(d[item]) / len(d[item])
    if media < 5:
        c[item] = media  # creez un dict nou cu corigentii si media

for i in sorted(c):
    print('{:12} {:12}   {:0.2f}'.format(i.split()[0], i.split()[1], sum(d[i]) / len(d[i])))

print("-" * 32)