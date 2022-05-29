
n = int(input("Introduceti un numar intreg >= 0: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(str(n) + "! = " + str(factorial))