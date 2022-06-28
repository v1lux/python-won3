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


class Rectangle:

    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def __eq__(self, other):
        if sorted(self.get_dimensions()) == sorted(other.get_dimensions()):
            return True
        return False

    def get_dimensions(self):
        l1 = self.p1.x - self.p2.x
        l2 = self.p1.y - self.p2.y
        return abs(l1), abs(l2)

    def get_rectangle_area(self):
        rectangle_area = self.get_dimensions()[0] * self.get_dimensions()[1]
        return rectangle_area

    def get_perimeter(self):
        perimeter = 2 * self.get_dimensions()[0] + 2 * self.get_dimensions()[1]
        return perimeter

    def point_inside(self, p: Point):
        x_min = min(self.p1.x, self.p2.x)  # marginea din stanga
        x_max = max(self.p1.x, self.p2.x)  # marginea din dreapta
        y_min = min(self.p1.y, self.p2.y)  # marginea de jos
        y_max = max(self.p1.y, self.p2.y)  # marginea de sus
        if (x_min <= p.x <= x_max) and (y_min <= p.y <= y_max):
            return True
        return False

    def circle_inside(self, c: Circle):
        x_min = min(self.p1.x, self.p2.x)  # marginea din stanga
        x_max = max(self.p1.x, self.p2.x)  # marginea din dreapta
        y_min = min(self.p1.y, self.p2.y)  # marginea de jos
        y_max = max(self.p1.y, self.p2.y)  # marginea de sus
        if x_min <= (c.x - c.r) and (c.x + c.r) <= x_max and y_min <= (c.y - c.r) and (c.y + c.r) <= y_max:
            return True
        return False


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


