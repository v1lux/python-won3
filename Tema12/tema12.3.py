from geometry import Point, get_coordinates

x1, y1 = get_coordinates(1)
x2, y2 = get_coordinates(2)

p1 = Point(x1, y1)
p2 = Point(x2, y2)
d1 = p1.get_distance()
d2 = p2.get_distance()

if d1 > d2:
    print('p1 este mai departe de centru decat p2')
elif d1 < d2:
    print('p2 este mai departe de centru decat p1')
else:
    print('p1 si p2 sunt la aceeasi distanta fata de centru')


