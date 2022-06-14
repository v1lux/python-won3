from geometry import Point, Circle


def bubble_sort(ls):
    for i in range(len(ls)):
        for j in range(len(ls) - 1):
            if ls[j].get_distance() > ls[j + 1].get_distance():
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
    return ls


def display_results(lst):
    for item in lst:
        print(f"Coordonate: {item.x}, {item.y}  Distanta: {item.get_distance()}")
    print("-" * 50)

p1 = Point(9, 12)
p2 = Point(6, 8)
p3 = Point(3, 4)

# p1 = Point(4, 8.5)
# p2 = Point(3, 4)
# p3 = Point(-5, 6)
c1 = Circle(3, 4, 2)
c2 = Circle(3, 4, 3)
# l = [p1, p2, p3]
l = [p1, p2, p3, c1, c2]


# sl = sorted(l, key=Point.get_distance)      # key - nu merge cand sunt amestecate puncte si cercuri
# display_results(sl)

# sl2 = sorted(l, key=lambda x: x.get_distance())  # key, lambda
# display_results(sl2)

# sl3 = bubble_sort(l)        # bubble sort
# display_results(sl3)





