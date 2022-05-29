# a)
ls = ['5', '123', '-7', '33']
li = [5, 123, -7, 33]

print(sorted(ls))
print(sorted(ls, key=int))
print(sorted(li))

# b)
l = [(5, 21, 8), (6, 11, -5), (0, 25, 3), (-6, 6, 1)]
print(sorted(l, key=sum))
