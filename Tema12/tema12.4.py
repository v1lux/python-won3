from geometry import Circle, get_coordinates, get_ray

x, y = get_coordinates()
r = get_ray()
c = Circle(x, y, r)

print(f'Distanta cercului fata de baza este: {c.get_distance()}')
print(f'Aria cercului este: {c.get_area()}')
