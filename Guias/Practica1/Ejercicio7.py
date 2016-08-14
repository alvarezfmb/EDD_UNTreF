def contarCaracteres(string):  # en clase
    result = {}  # llaves porque es diccionario maestro
    for x in string:
        # Python Docs: Return the value for key if key is in the dictionary, else default.
        # Defino default como 0
        apariciones = result.get(x, 0)
        result[x] = apariciones + 1
    return result


# Reciba ademas de la cadena de caracteres un caracter k y devuelva la frecuencia de k
# en la cadena (si k no aparece debe devolver 0)

def contarCaracteresAndCheckK(string, k):
    result = {}  # llaves porque es diccionario maestro
    for x in string:
        # Python Docs: get --> Return the value for key if key is in the dictionary, else default.
        # Defino default como 0
        apariciones = result.get(x, 0)
        result[x] = apariciones + 1
    return result, k + ": " + str(result.get(k, 0))


# Devuelva un diccionario cuyas claves sean las vocales y los valores una lista de palabras
# que empiecen con la vocal dada(suponer que dentro de la cadena las palabras estan
# separadas por coma y no hay espacios intermedios).

# recibe cadena de palabras separadas por coma
def vocales(string):
    vocales = {"A": [], "E": [], "I": [], "O": [], "U": []}
    tokens = string.upper().split(",")
    for item in tokens:
        if item[0] in vocales:
            vocales[item[0]].append(item)
    return vocales

    # string = "ana,enano,oso,ala,indio,asado"
    # print(vocales(string))
