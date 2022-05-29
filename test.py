# this is a test program

print('Hello GitHub')

def is_even(nr):
    """Functia is_even.

    Parameters:
    ----------
    nr : int
        numarul de verificat

    Returns:
    ----------
    bool :
        returneaza True daca nr e par si False daca e impar

    Example usage:
    ----------
    >>> is_even(9)
    False
    >>> is_even(22)
    True
    """

    return not bool(nr % 2)

a = is_even(22)
print(type(a))
print(a)

