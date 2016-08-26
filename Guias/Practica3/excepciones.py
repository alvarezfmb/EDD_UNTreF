# funcion que levanta IndexError


def oops():
    list = [1, 2]
    print(list[10])


def llamada_a_oops():
    try:
        oops()
    except IndexError:  # si escribo solo except me ataja cualquier tipo de excepcion
        print("Excepcion salvada")


if __name__ == '__main__':
    llamada_a_oops()
