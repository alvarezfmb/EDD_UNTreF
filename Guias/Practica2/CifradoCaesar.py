from Guias.Practica2.Caesar import Cifrador


class CifradorCesar(Cifrador):
    """Cifrador que usa la tecnica de Ceasar, reemplaza cada caracter
    siempre por el mismo caracter, desplazando cada letra una cantidad
    fija

    A diferencia del original, la clave siempre es 13.
    """

    clave = 13

    def __init__(self):
        Cifrador.__init__(self, 13, "Cifrado Caesar")


if __name__ == '__main__':
    caesar = CifradorCesar()
    print("Tipo: ", caesar.tipo)
    print("Clave: ", caesar.clave)
    print(caesar.cifrar("abcdefghijklmnopqrstuvwxyz", CifradorCesar.clave))
