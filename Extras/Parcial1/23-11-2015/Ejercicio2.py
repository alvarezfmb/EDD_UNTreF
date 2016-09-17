import pickle


# Escribir una función que reciba una matriz de adyacencia y devuelva un diccionario que represente la lista de
# adyacencia correspondiente, donde las claves son los números de nodos y los valores una lista de tuplas
# (nodo_destino, peso)
# {1: [(2,1),(3,2)]}


def crear_dicc_de_adyacencia(lst):
    ''' :param lst: lista de listas representando filas de matriz de adyacencia '''
    dicc = {}
    for i, row in enumerate(lst, start=1):
        dicc[i] = []
        for j, item in enumerate(row, start=1):
            if item != 0:
                dicc[i].append((j, item))
    return dicc


# Escribir una función que reciba una matriz de adyacencia y devuelva un diccionario con los grado de entrada
# de cada nodo (el grado de entrada es la cantidad de aristas que llegan a un nodo)


def contar_aristas(lst):
    dicc = {}
    # for i, row in enumerate(lst, start=1):
    #     dicc[i] = 0
    for i in range(1, len(lst) + 1):
        dicc[i] = 0
    for i, row in enumerate(lst, start=1):
        for j, item in enumerate(row, start=1):
            if item != 0:
                dicc[j] += 1
    return dicc


# Escribir una función guardar_grafo_en_disco que recibe un diccionario con la lista de adyacencia y un
# nombre de archivo.


def guardar_grafo(dicc, archivo):
    pickle.dump(dicc, open(archivo, 'wb'))


def abrir_grafo(archivo):
    dicc = pickle.load(open(archivo, 'rb'))
    print(dicc)


if __name__ == '__main__':
    lst = [[0, 1, 2, 0, 0], [0, 0, 4, 0, 0], [0, 0, 0, 0, 4], [0, 0, 0, 0, 5], [0, 0, 0, 0, 0]]
    print(crear_dicc_de_adyacencia(lst))
    print(contar_aristas(lst))
    dicc = crear_dicc_de_adyacencia(lst)
    guardar_grafo(dicc, 'grafo.p')
    abrir_grafo('grafo.p')
