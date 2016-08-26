# funcion que levanta IndexError


def oops():
    list = [1, 2]
    print(list[10])


def llamada_a_oops():
    try:
        oops()
    except IndexError:  # si escribo solo except me ataja cualquier tipo de excepcion
        print("Excepcion salvada")


def ejercicio5sub1():
    try:
        oops()
    except IndexError:
        print("Index")
    else:
        print("else")  # se imprime si HAY error


def ejercicio5sub2():
    try:
        oops()
        print("ej")  # se imprime si NO HAY error, no se imprime si HAY error
    except IndexError:
        print("Index")


if __name__ == '__main__':
    # llamada_a_oops()
    ejercicio5sub1()
    # ejercicio5sub2()
