import pickle


# La clase persona tiene atributos nombre, apellido y DNI. Para poder guardar en disco una serie de personas las
# representaremos dentro de un diccionario de la siguiente manera: cada persona tiene como clave su DNI y como valor
# un diccionario con su nombre y apellido.
# {5678: {'nombre': 'juan', 'apellido': 'perez'}, 910112: {'nombre': 'ana', 'apellido': 'lia'}}

# Escribir una función agregar_persona a un diccionario de personas.


class Persona:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni


class Agenda:
    def __init__(self, dicc={}):
        self.dicc = dicc

    def agregar_persona(self, persona):
        if persona.dni not in self.dicc:
            self.dicc[persona.dni] = {}
            self.dicc[persona.dni]['nombre'] = persona.nombre
            self.dicc[persona.dni]['apellido'] = persona.apellido

    def guardar(self):
        pickle.dump(self.dicc, open('agenda.p', 'wb'))

    def abrir(self):
        self.dicc = pickle.load(open('agenda.p', 'rb'))

    def mostrar(self):
        for k, v in self.dicc.items():
            print('Nombre y apellido:', v['nombre'], v['apellido'], '| DNI:', k)


if __name__ == '__main__':
    # ana = Persona('Ana', 'Bla', 18800900)
    # pepe = Persona('Pepe', 'Perez', 30100200)
    agenda = Agenda()
    # agenda.agregar_persona(ana)
    # agenda.agregar_persona(pepe)
    # print(agenda.dicc)
    # agenda.guardar()
    agenda.abrir()
    print(agenda.dicc)
    agenda.mostrar()
