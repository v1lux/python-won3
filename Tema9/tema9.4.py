"""
4. Creati un comprehension care sa genereze o lista continand toate numerele din intervalul 0-100 care sunt divizibile cu 3 și nu
sunt divizibile cu 5.
"""

result = [x for x in range(0, 101) if not x % 3 and x % 5]

print(result)