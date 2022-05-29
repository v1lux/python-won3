def is_even(nr):
    """Functia is_even.

    Parameters:
    ----------
    nr : int
        numarul de verificat

    Returns:
    ----------
    boolean :
        returneaza True daca nr e par si False daca e impar

    Example usage:
    ----------
    >>> is_even(9)
    False
    >>> is_even(22)
    True
    """

    return not bool(nr % 2)


if __name__ == '__main__':
    from doctest import testmod
    testmod()
    testmod(name='is_even', verbose=True)
    print(is_even(100))
