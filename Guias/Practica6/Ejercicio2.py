import functools

# Dado una lista de tuplas (articulo, cant, precio_unitario) calcular el monto total de venta


def calcular_venta(lst):
    # map mapea cada tupla con su valor total de venta
    l = list(map(lambda x: x[1]*x[2], lst))
    # reduce suma todas las ventas
    return functools.reduce(lambda x, y: x+y, l)


if __name__ == '__main__':
    print(calcular_venta([('art1', 10, 100), ('art2', 20, 2), ('art3', 5, 150)]))
