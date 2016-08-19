import string

class Cifrador(object):
    def __init__(self, clave=0, tipo=""):
        """Las subclases pueden tener diferentes tipos de claves
        tipo es una cadena, por ejemplo "Caesar"
        """
        self.clave = clave
        self.tipo = tipo

    def __str__(self):
        """La representacion de un cifrador es su tipo
        """
        return ("Cifrador " + self.tipo)

    def cifrar(self, frase, clave):
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
            if indice == -1:  # si no es letra minuscula, permanece inalterada
                frase_cifrada += l
            else:
                if (indice + clave) > len(string.ascii_lowercase) - 1:  # si se pasa, resto longitud de cadena
                    # resto 1 porque len() cuenta desde 1
                    clave -= len(string.ascii_lowercase)
                    frase_cifrada += string.ascii_lowercase[indice + clave]
                else:
                    frase_cifrada += string.ascii_lowercase[indice + clave]
        return frase_cifrada

    def descifrar(self, frase_cifrada, clave):
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

    def cifrar_archivo(self, entrada, salida, clave):
        """ Cifra el archivo de entrada usando la tecnica de Caesar

        Argumentos:
        entrada: cadena de caracteres con el path completo al archivo
        de entrada
        salida: cadena de caracteres con el path completo al archivo
        de salida
        clave: entero entre 0 y 26
        """
        texto_cifrado = ""
        archivo_entrada = open(entrada, "r")
        for line in archivo_entrada:
            texto_cifrado += self.cifrar(line, clave)
        archivo_entrada.close()
        archivo_salida = open(salida, "w")
        for line in texto_cifrado:
            archivo_salida.write(line)

    def descifrar_archivo(self, entrada, salida, clave):
        """ Descifra el archivo de entrada usando la tecnica de Caesar

        Argumentos:
        entrada: cadena de caracteres con el path completo al archivo
        de entrada
        salida: cadena de caracteres con el path completo al archivo
        de salida
        clave: entero entre 0 y 26
        """
        texto_descifrado = ""
        archivo_entrada = open(entrada, "r")  # archivo de entrada contiene texto previamente cifrado
        for line in archivo_entrada:
            texto_descifrado += self.descifrar(line, clave)
        archivo_entrada.close()
        archivo_salida = open(salida, "w")
        for line in texto_descifrado:
            archivo_salida.write(line)


if __name__ == '__main__':
    ruta_entrada = "/Users/fmbalvarez/PycharmProjects/EDD_UNTreF/Guias/Practica2/entrada.txt"
    ruta_salida = "/Users/fmbalvarez/PycharmProjects/EDD_UNTreF/Guias/Practica2/salida.txt"
    salida_de_descifrado = "/Users/fmbalvarez/PycharmProjects/EDD_UNTreF/Guias/Practica2/salida_de_descifrado.txt"
    cifrador = Cifrador()
    cifrador.cifrar_archivo(ruta_entrada, ruta_salida, 1)
    cifrador.descifrar_archivo(ruta_salida, salida_de_descifrado, 1)
    print(cifrador.__str__())
