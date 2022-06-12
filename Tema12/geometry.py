class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self):
        distance = (self.x ** 2 + self.y ** 2) ** 0.5
        return f'{distance:.2f}'


class Circle(Point):

    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def get_area(self):
        area = 3.14 * self.r ** 2
        return area

    def get_distance(self):
        dst = super().get_distance()
        return f'{float(dst) - self.r:.2f}'


def get_coordinates(*args):
    if args:
        x = int(input(f"Introdu valoare coordonatei x{args[0]}: "))
        y = int(input(f"Introdu valoare coordonatei y{args[0]}: "))
    else:
        x = int(input(f"Introdu valoare coordonatei x: "))
        y = int(input(f"Introdu valoare coordonatei y: "))
    return x, y


def get_ray():
    r = int(input(f"Introdu valoare razei: "))
    return r

