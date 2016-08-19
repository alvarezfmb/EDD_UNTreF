import string


def cifrar(frase, clave):
    """ Cifra una frase usando la tecnica de Caesar, desplazando cada
    letra la cantidad de caracteres indicado en la clave.

    Argumentos:
        frase: cadena de caracteres a cifrar (solo letras minusculas)
        clave: un entero con la cantidad de posiciones a desplazar (entre 0
        y 26)

    Retorno:
        Devuelve una cadena de caracteres con la frase cifrada. Si la
        frase original contenia otros caracteres que no fueran letras
        minusculas estos quedan inalterados en la cadena retornada
    """
    frase_cifrada = ""
    for l in frase:
        indice = string.ascii_lowercase.find(l)
        if indice == -1:
            frase_cifrada += l
        else:
            if (indice + clave) > len(string.ascii_lowercase) - 1:
                clave -= len(string.ascii_lowercase)
                frase_cifrada += string.ascii_lowercase[indice + clave]
            else:
                frase_cifrada += string.ascii_lowercase[indice + clave]
    return frase_cifrada


def descifrar(frase_cifrada, clave):
    """ Devuelve la frase descifrada con la clave aplicando el metodo
    Ceasar

    Argumentos:
        frase_cifrada: frase cifrada con el metodo Ceasar y la clave
        clave: clave para descifrar, debe ser igual a la usada cuando
        se cifro

    Retorna:
        frase descifrada
    """
    frase_descifrada = ""
    for l in frase_cifrada:
        indice = string.ascii_lowercase.find(l)
        if indice == -1:
            frase_descifrada += l
        else:
            frase_descifrada += string.ascii_lowercase[indice - clave]
    return frase_descifrada
