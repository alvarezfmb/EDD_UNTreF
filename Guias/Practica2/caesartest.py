import unittest, random

from Guias.Practica2.caesar import Cifrador  # se importa con punto!


class TestCaesar(unittest.TestCase):
    def setUp(self):
        self.frases = ["Rosita Wachenchauzer", "estructura de datos"]
        self.cifradas3 = ["Rrvlwd Wdfkhqfkdxchu", "hvwuxfwxud gh gdwrv"]

    def test_clave_cero(self):
        """Asegurarse que con clave 0 nos da la misma frase
        """
        for f in self.frases:
            self.assertEqual(Cifrador.cifrar(f, 0), f)

    def test_cifrar(self):
        """Asegurarse que cifra bien con frases (sin normalizar) conocidas
        """
        clave = 3
        for i in range(len(self.frases)):
            self.assertEqual(Cifrador.cifrar(self.frases[i], clave), self.cifradas3[i])

    def test_cifrar_descifrar(self):
        """Asegurarse que si ciframos y desciframos con la misma clave
        se obtiene de nuevo la frase original
        """
        clave = random.randint(0, 26)
        for f in self.frases:
            self.assertEqual(Cifrador.descifrar(Cifrador.cifrar(f, clave), clave), f)

    if __name__ == "__main__":
        unittest.main()
