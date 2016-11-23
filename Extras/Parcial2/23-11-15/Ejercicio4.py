# 4. Se tienen datos de ventas del día en un archivo csv con el siguiente formato:
#
# artículo, cantidad, precio_unitario
#
# (a) Explicar en qué consiste el esquema Map/Reduce.
# (b) Escribir en Python dos funciones Map y Reduce para calcular el monto total de la venta (el Map debe generar un
# archivo intermedio adecuado).

import csv

# MAP: leo csv y genero tuplas (producto, precio_unitario * cantidad) // nombre de produco necesario?
# REDUCE: devuelve monto total sumando lista de precios unitarios


def leer_csv(nombre_archivo):  # map
    file = open(nombre_archivo, 'r')
    next(file)
    reader = csv.reader(file, delimiter=';')
    lst_intermedia = []
    for line in reader:
        lst_intermedia.append((line[0], int(line[1]) * int(line[2])))
    return lst_intermedia

def reduce(lst_intermedia):
    total = 0
    for item in lst_intermedia:
        total += item[1]
    return total

if __name__ == '__main__':
    x = leer_csv('comercio.csv')
    print(x)
    print('Total', reduce(x))