class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self):
        distance = (self.x ** 2 + self.y ** 2) ** 0.5
        return round(distance, 2)


class Circle(Point):

    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def get_area(self):
        area = 3.14 * self.r ** 2
        return area

    def get_distance(self):
        return super().get_distance() - self.r


def get_coordinates(*args):
    if args:
        x = float(input(f"Introdu valoare coordonatei x{args[0]}: "))
        y = float(input(f"Introdu valoare coordonatei y{args[0]}: "))
    else:
        x = float(input(f"Introdu valoare coordonatei x: "))
        y = float(input(f"Introdu valoare coordonatei y: "))
    return x, y


def get_ray():
    r = float(input(f"Introdu valoare razei: "))
    return r

