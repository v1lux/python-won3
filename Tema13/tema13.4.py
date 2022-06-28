from geometry import Point, Rectangle, Circle, get_coordinates, get_ray

x1, y1 = get_coordinates(1)
x2, y2 = get_coordinates(2)
x, y = get_coordinates()
r = get_ray()

p1 = Point(x1, y1)
p2 = Point(x2, y2)
c = Circle(x, y, r)

r1 = Rectangle(p1, p2)

print(f'Este cercul inclus in dreptunghi? -> {r1.circle_inside(c)}')
