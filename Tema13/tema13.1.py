from geometry import Point, Rectangle, get_coordinates

x1, y1 = get_coordinates(1)
x2, y2 = get_coordinates(2)

p1 = Point(x1, y1)
p2 = Point(x2, y2)

r1 = Rectangle(p1, p2)

print(f'\ndimensiunile laturilor dreptunghiului: {r1.get_dimensions()[0]}, {r1.get_dimensions()[1]}')
print(f'aria: {r1.get_rectangle_area()}')
print(f'perimetrul: {r1.get_perimeter()}')