# Escribir una funcion en Python que reciba una lista de cadenas y devuelva un ındice invertido,
# considerando que la primera cadena de la lista es la 0, la siguiente la 1, etc.


def indice_invertido(lista_de_strings):
    dicc_indice_invertido = {}
    for i, s in enumerate(lista_de_strings):
        s_normalizado = normalizar(s)
        for palabra in s_normalizado:
            if palabra not in dicc_indice_invertido:
                dicc_indice_invertido[palabra] = []
                dicc_indice_invertido[palabra].append(i)
            elif not dicc_indice_invertido[palabra].__contains__(i):
                dicc_indice_invertido[palabra].append(i)
    return dicc_indice_invertido


def normalizar(string):
    return string.lower().split()


if __name__ == '__main__':
    lista = ['Habia una vez un barco chiquito', 'Una que otra vez un ice-berg hunde un barco',
             'Decir barco es de burgues']
    print(indice_invertido(lista))
