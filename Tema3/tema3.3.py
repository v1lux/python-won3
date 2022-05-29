
my_list = [2, 5.7, 33, 101.1, 48, 22.2, -7, 0]
second_list = [2, 5.7, 33, 101.1, 48, 22.2, -7, 0]

my_list.sort()
print("a) Solutie folosind functia sort():")
print("minim: " + str(my_list[0]))
print("maxim: " + str(my_list[len(my_list) - 1]))
print("===========================================")

maxim = float('-inf')
minim = float('inf')
for i in range(len(second_list)):
    if second_list[i] > maxim:
        maxim = second_list[i]

    if second_list[i] < minim:
        minim = second_list[i]

print("b) Solutie folosind un algoritm de sortare:")
print("min: " + str(minim))
print("max: " + str(maxim))
print("===========================================")

print("c) Nu putem avea stringuri in lista pentru ca nu se pot compara cu int/float.")

