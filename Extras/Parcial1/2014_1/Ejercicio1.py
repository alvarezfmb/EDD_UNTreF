# Se tiene un archivo de texto que contiene palabras separadas por blancos y se quiere armar un diccionario cuyas claves
#  son las palabras y cuyos valores son la lista de los números de línea en donde aparece cada una de las palabras.
# Escribir una función Python que recibe el nombre del archivo y devuelve el diccionario pedido.


def indice_invertido():
    dicc = {}
    file = open('archivo.txt', 'r')
    for line_num, line in enumerate(file, start=1):
        word_tuple = line.lower().split()
        for word in word_tuple:
            word.strip()
            if word not in dicc:
                dicc[word] = []
            dicc[word].append(line_num)
    return dicc


if __name__ == '__main__':
    indice_invertido()
    print(indice_invertido())
