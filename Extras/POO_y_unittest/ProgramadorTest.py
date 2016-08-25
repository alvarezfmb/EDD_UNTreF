import unittest

from Extras.POO_y_unittest.Programador import Programador  # hay que importar clase especificamente, si no da TypeError


class ProgramadorTest(unittest.TestCase):
    def test_edad(self):
        programador = Programador("Pablo", 30)
        self.assertEqual(programador.edad, 30, "Mensaje informativo para consola")

    def test_booleano(self):
        programador = Programador("Pablo", 30)
        self.assertTrue(programador.empleado)


if __name__ == '__main__':
    unittest.main()  # para ejecutar test en consola. Si no el pycharm usa el plugin, pero this is better
