"""
3. Folosind functia map și o functie lambda scrieti o expresie care sa transforme listele acestea:
[2, 3, 1]
[1, 4, 5]
['A', 'q', '#']
în asta
['AAA', 'qqqqqqq', '######']
"""


a = [2, 3, 1]
b = [1, 4, 5]
c = ['A', 'q', '#']

result = list(map(lambda x, y, z: (x + y) * z, a, b, c))
print(result)