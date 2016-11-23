import functools

# Dada una lista de enteros encontrar el producto de los elementos de la lista elevados al cubo


def producto_cubos(lista):
    l = list(map(lambda x: x ** 3, lista))
    return functools.reduce(lambda x, y: x*y, l)


if __name__ == '__main__':
    # functools.reduce
    # Apply function of two arguments cumulatively to the items of sequence, from left to right, so as to reduce
    # the sequence to a single value. For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    # ((((1+2)+3)+4)+5). The left argument, x, is the accumulated value and the right argument, y, is the update value
    # from the sequence. If the optional initializer is present, it is placed before the items of the sequence in the
    # calculation, and serves as a default when the sequence is empty. If initializer is not given and sequence contains
    #  only one item, the first item is returned.
    print(functools.reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))

    # map
    # Return an iterator that applies function to every item of iterable, yielding the results.
    # If additional iterable arguments are passed, function must take that many arguments and is applied to the items
    # from all iterables in parallel. With multiple iterables, the iterator stops when the shortest iterable is
    # exhausted. For cases where the function inputs are already arranged into argument tuples, see itertools.starmap().
    l = map(lambda x: x**2, [1, 2, 3, 4, 5])
    print(list(l))  # devuelve objeto map, lo convierto a lista
    # es equivalente a:
    lista_cuadrados = [x**2 for x in [1, 2, 3, 4, 5]]
    print(lista_cuadrados)

    # mapreduce
    l = list(map(lambda x: x*x, [1, 2, 3, 4, 5]))
    mr = functools.reduce(lambda x, y: x+y, l, 0)
    print(mr)

    # test max
    l = [3, 15, 9, 18, 33, 2, 1, 0, 5, 19]
    print(functools.reduce(lambda x,y: max(x,y), l))

    # no necesariamente reduce necesita funciones lambda
    # ej 1
    print('Ejercicio 1 \n', producto_cubos([1, 2, 3]))
