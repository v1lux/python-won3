l = [1, 2, 4, 5, 3]
suma = sum([x for x in l[::2] if not x % 2])
print(suma)
print(sum([x for x in [1, 2, 4, 5, 3][::2] if not x % 2]))

