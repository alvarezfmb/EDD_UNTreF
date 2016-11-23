import pickle

# diccionario de recetas de comida clave nombre de plato, valor lista de pares (ingred, cant) como cant para una
# porcion. Se tiene otro dicc con productos en mi alacena con clave ingrediente y valor cantidad disponible.

# (a) dado una lista que_se_cocina que contiene pares (plato, cantidad de porciones) construir un dicc de compras
# con los ingredientes que faltan para cocinar

# (b) escribir funciones para hacer persistente el dicc

recetas = {'pizza': [('harina', 30), ('tomate', 1), ('queso', 25)],
           'ensalada': [('lechuga', 100), ('tomate', 1), ('zanahoria', 1)]}
alacena = {'huevo': 6, 'harina': 500, 'queso': 250, 'tomate': 2}
que_se_cocina = [('pizza', 2), ('ensalada', 2)]


def lista_de_compras():
    dicc_compras = {}
    for plato in que_se_cocina:
        nombre_plato = plato[0]
        porciones = plato[1]
        lista_receta = recetas[nombre_plato]
        for tupla in lista_receta:
            ingrediente = tupla[0]
            cantidad = tupla[1]
            if ingrediente not in alacena:  # si no lo tengo, lo agrego directamente a dicc de compras
                if ingrediente not in dicc_compras:
                    dicc_compras[ingrediente] = 0
                dicc_compras[ingrediente] += (cantidad * porciones)
            elif (cantidad * porciones) > alacena[ingrediente]:  # si necesito mas que lo que tengo, agrego en dicc
                if ingrediente not in dicc_compras:
                    dicc_compras[ingrediente] = 0
                # agrego a compras lo que necesito menos lo que tengo
                dicc_compras[ingrediente] += (cantidad * porciones) - alacena[ingrediente]
                # redefino la cantidad de lo que tengo en alacena
                alacena[ingrediente] = 0
            else: # si tengo lo necesario o igual, resto de alacena
                alacena[ingrediente] -= cantidad * porciones
    print(alacena)
    return dicc_compras


def guardar(x):
    with open('persistencia.p', 'wb') as handle:
        pickle.dump(x, handle)


def abrir():
    with open('persistencia.p', 'rb') as handle:
        x = pickle.load(handle)
    return x


if __name__ == '__main__':
    print(lista_de_compras())
    # x = lista_de_compras()
    # guardar(x)
    # print(abrir())
    #
    # file = open('informe.txt', 'w')
    # lst = ['1','2']
    # for x in lst:
    #     print(x, file=file)
    # file.close()
