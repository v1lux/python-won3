from geometry import Point, Rectangle, get_coordinates

# x1, y1 = get_coordinates(1)
# x2, y2 = get_coordinates(2)
# x3, y3 = get_coordinates(3)
# x4, y4 = get_coordinates(4)

x1, y1, x2, y2, x3, y3, x4, y4 = -11, 2, 0, 0, 3, 2, 0, 0  # false
#x1, y1, x2, y2, x3, y3, x4, y4 = -3, 2, 0, 0, 0, 0, 2, 3  # true


p1 = Point(x1, y1)
p2 = Point(x2, y2)
p3 = Point(x3, y3)
p4 = Point(x4, y4)

r1 = Rectangle(p1, p2)
r2 = Rectangle(p3, p4)

print(f'are the rectangles equal?\n{r1 == r2}')
