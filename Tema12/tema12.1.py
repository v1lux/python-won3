class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self):
        distance = round((self.x ** 2 + self.y ** 2) ** 0.5, 2)
        return f'{distance:.2f}'


x = float(input("Introdu valoare coordonatei x: "))
y = float(input("Introdu valoare coordonatei y: "))

p = Point(x, y)
print(f'Distanta de la punct la origine este {p.get_distance()}')
