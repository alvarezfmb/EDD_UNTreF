from Extras.POO_y_unittest.Empleado import Empleado


class Programador(Empleado):
    def __init__(self, nombre, edad):
        super(Programador, self).__init__(nombre, edad, True)  # uso super para llamar al init de clase padre

    def probar_super(self):
        self.probar_default()


if __name__ == '__main__':
    monkey = Programador("Monkey", 20)
    print(monkey.labura())  # puedo acceder a metodos de la clase padre
    monkey.probar_super()  # el error del None era por doble print
    monkey.probar_default()
    print("Atributo: ", monkey.attr)  # puedo acceder a elementos estaticos de la clase padre
    monkey.saludar()
    emp = Empleado("Albarra", 40)
    emp.probar_default()
    monkey.probar_super()
