# Se tiene

# (a) un diccionario con los artefactos de la casa, con el nombre del artefacto como clave y el estado
# (“Funciona” o “No Funciona”) como valor (por ejemplo {“pincel brocha gorda”: “Funciona”, “escalera”:
# “Funciona”,”rodillo”: “No Funciona”, “martillo”: “Funciona”})

# (b) un diccionario con los materiales
# disponibles en la casa, con el nombre del material como clave y la cantidad disponible como valor (por
# ejemplo {“pintura blanca”:2, “clavos de 0,5”: 100, “lija fina”: 4})

# (c) un diccionario de arreglos que tiene
# como clave el tipo de arreglo y como valor un par con una lista de artefactos y una lista de materiales con
# las cantidades que se consumen para cada arreglo (los artefactos no se consumen: alcanza con tener uno
# que funcione para poder hacer el arreglo).

# (I) Construir una lista de compras, es decir un diccionario que tenga como claves los materiales y/o artefactos
# que tengo que comprar para poder hacer los arreglos.

# Por ejemplo, si el diccionario de arreglos es {“pintar
# pieza chicos”: ([“rodillo”, “pincel brocha gorda”, “pincel brocha fina”, “escalera”], [(“pintura blanca”, 3),
# (“lija fina”, 1)]), “pintar comedor”: ([“rodillo”, “pincel brocha gorda”, “pincel brocha fina”, “escalera”],
# [(“pintura blanca”, 4), (“lija fina”, 1)])}, la lista de compras será {“rodillo”: 1, “pincel brocha fina”: 1,
# “pintura blanca”: 5 }


def construir_lista_de_compras(dicc_artefactos, dicc_materiales, dicc_arreglos):
    dicc_compras = {}
    for arreglo in dicc_arreglos.items():
        for artefacto in arreglo[1][0]:
            if artefacto not in dicc_artefactos or dicc_artefactos[artefacto] == 'No Funciona':
                dicc_compras[artefacto] = 1
        for material in arreglo[1][1]:
            if material[1] > dicc_materiales[material[0]]:
                dicc_compras[material[0]] = abs(dicc_materiales[material[0]] - material[1])
                dicc_materiales[material[0]] -= material[1]
    return dicc_compras


if __name__ == '__main__':
    dicc_artefactos = {'pincel brocha gorda': 'Funciona', 'escalera': 'Funciona', 'rodillo': 'No Funciona',
                       'martillo': 'Funciona'}
    dicc_materiales = {'pintura blanca': 2, 'clavos de 0,5': 100, 'lija fina': 4}
    dicc_arreglos = {'pintar pieza chicos': (['rodillo', 'pincel brocha gorda', 'pincel brocha fina', 'escalera'],
                                             [('pintura blanca', 3), ('lija fina', 1)]),
                     'pintar comedor': (
                         ['rodillo', 'pincel brocha gorda', 'pincel brocha fina', 'escalera'], [('pintura blanca', 4),
                                                                                                ('lija fina', 1)])}
    dicc = construir_lista_de_compras(dicc_artefactos, dicc_materiales, dicc_arreglos)
    print(dicc)
