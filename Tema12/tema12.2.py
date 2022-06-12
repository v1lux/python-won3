from geometry import Point, get_coordinates

x, y = get_coordinates()
p = Point(x, y)
print(f'Distanta de la punct la origine este {p.get_distance()}')
