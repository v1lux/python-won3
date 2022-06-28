from geometry import Point, Rectangle, get_coordinates

x1, y1 = get_coordinates(1)
x2, y2 = get_coordinates(2)
x, y = get_coordinates()

p1 = Point(x1, y1)
p2 = Point(x2, y2)
p = Point(x, y)

r1 = Rectangle(p1, p2)

print(f'Este punctul inclus in dreptunghi? -> {r1.point_inside(p)}')
