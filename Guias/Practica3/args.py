import sys


def segura1(func, *pargs, **kwargs):
    try:
        for x in pargs:
            func(x)
        for x, y in kwargs.items():
            print(x, ":", y)
    except:
        print("Excepcion atrapada:", sys.exc_info()[0])  # imprime por partes el informe de sys
        print(sys.exc_info()[1])
        print(sys.exc_info()[2])


def imprimir_y_sumar(i):
    print(i + 1)


if __name__ == '__main__':
    segura1(imprimir_y_sumar, 1, 2, 3, a="aa", b="bb")  # items de kwargs los toma en cualquier orden, es un dic
    # si paso un string en vez de numeros para *args devuelve informe de error
    # segura1(imprimir_y_sumar, 1, "hola", 3, a="aa", b="bb")
