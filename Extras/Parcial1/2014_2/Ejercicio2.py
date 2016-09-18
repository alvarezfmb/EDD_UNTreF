# Se tiene un archivo de texto formado por líneas compuestas por números enteros positivos separados por comas.
# Escribir una función que lea el archivo y genere un diccionario que indique en qué líneas el máximo está
# entre 0 y 9 (clave 1), en qué líneas el máximo está entre 10 y 19 (clave 10), etc
# la salida deberá ser: {100: [1, 4], 1: [2,3]}.


def dicc_maximos():  # tip to Guid1OS
    dicc = {}
    file = open('archivo.txt', 'r')
    for i, line in enumerate(file, start=1):
        lista_split = line.split(',')
        lista_split = [int(x) for x in lista_split]
        maximo = max(lista_split)
        if maximo < 10:
            if 1 not in dicc:
                dicc[1] = []
            dicc[1].append(i)
        else:
            maximo = str(maximo)
            clave = str(maximo[0])
            for j in range(1, len(maximo)):
                clave += '0'
            if clave not in dicc:
                dicc[clave] = []
            dicc[clave].append(i)
    return dicc


if __name__ == '__main__':
    print(dicc_maximos())
