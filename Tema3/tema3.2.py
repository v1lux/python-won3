
my_list = ['ABCD', '12', 'w', ':-)']
reversed_list = []

for string in my_list:
    reversed_s = []

    for char in string:
        reversed_s.insert(0, char)
    rs = ''.join(reversed_s)
    reversed_list.insert(0, rs)

print(reversed_list)