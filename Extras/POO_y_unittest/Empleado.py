class Empleado:
    attr = "atributo"  # elemento estaticos. Igual lo puedo cambiar porque anarquia

    # si modifico un attr estatico se modifica para todas las instancias de esa clase posteriormente creadas

    def __init__(self, nombre, edad, empleado=False):
        # la buena practica es declarar dentro del init los elementos propios del objeto, o sea, el "self"
        # si modifico un atributo declarado en el init, solo se modifica para ese objeto
        self.nombre = nombre
        self.edad = edad
        self.empleado = empleado
        self.default = "Default"  # asi puedo declarar atributo propio del objeto

    def probar_default(self):
        print(self.default)

    def labura(self):
        return self.empleado

    def saludar(self):
        print("Hola")


if __name__ == '__main__':
    pedrito = Empleado("Pedro", 20)
    pedrito.probar_default()
    print(pedrito.labura())
    print(Empleado.attr)
    pedrito.attr = "te lo cambio"
    print(pedrito.attr)
    print(Empleado.attr)
    Empleado.attr = "te cambio el attr estatico"
    print(pedrito.attr)  # imprime lo mismo porque el objeto fue creado anteriormente
    jorgito = Empleado("Jorge", 20)
    print(jorgito.attr)  # ahora si, imprime el attr estatico modificado
