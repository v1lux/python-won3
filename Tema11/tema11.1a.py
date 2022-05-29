def media(lista_note):
    """Functia media.

    Parameters:
    ----------
    lista_note : list
        lista numerelor a caror medie o calculeaza functia

    Returns:
    ----------
    float :
        returneaza media numerelor din lista data ca parametru

    Example usage:
    ----------
    >>> media([7, 8, 9])
    8.0
    >>> media([9, 10])
    9.5
    """

    if len(lista_note) > 0:
        return round(sum(lista_note) / len(lista_note), 2)
    return 0


if __name__ == '__main__':
    from doctest import testmod
    testmod()
    testmod(name='media', verbose=True)


