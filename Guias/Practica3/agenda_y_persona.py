from Guias.Practica3.agendapicke import *
import shelve


class Agenda:
    def __init__(self):
        self.lista_agenda = []
        self.lista_personas = []

    def cargar_agenda_de_pickle(self):
        lista_agenda = abrir_pickle()
        for x in lista_agenda:
            persona = Persona(x[0], x[1]['Domicilio'], x[1]['Tel'], x[1]['Email'])
            self.lista_personas.append(persona)

    def crear_persona(self, nombre, domicilio, tel, *emails):
        persona = Persona(nombre, domicilio, tel, *emails)
        self.lista_personas.append(persona)
        self.guardar_shelve()  # personas con nombre (key) repetido no se agregan (shelve es diccionario)

    def listar_personas(self):
        db = shelve.open('shelve_db_agenda')
        for x in db.items():
            x[1].print_persona()  # x[1] porque devuelve tuplas con key y value

    def buscar_persona(self, nombre_buscado):
        db = shelve.open('shelve_db_agenda')
        return nombre_buscado in db

    def datos_persona(self, nombre_buscado):
        pos = self.buscar_persona(nombre_buscado)
        if pos == -1:
            print("No esta en la agenda")
        else:
            self.lista_personas[pos].__str__()

    def datos(self, nombre_buscado):
        db = shelve.open('shelve_db_agenda')
        if nombre_buscado not in db:
            return "No esta en agenda"
        else:
            db[nombre_buscado].print_persona()

    # TODO: metodo para modificar datos

    def guardar_shelve(self):
        '''
        Guarda personas en diccionario organizadas por nombre usando shelve
        '''
        db = shelve.open('shelve_db_agenda')
        for x in self.lista_personas:
            n = x.nombre
            print(n)
            db[x.nombre] = x
        db.close()


class Persona:
    def __init__(self, nombre, domicilio, tel, *emails):
        self.nombre = nombre
        self.domicilio = domicilio
        self.tel = tel
        self.emails = []
        for i in emails:
            self.emails.append(i)

    def print_persona(self):  # __str__ method should return string not print!
        print("Nombre:", self.nombre)
        print("Domicilio:", self.domicilio)
        print("Tel:", self.tel)
        print("Emails:", self.emails)


if __name__ == '__main__':
    agenda = Agenda()
    # agenda.cargar_agenda_de_pickle()
    # agenda.crear_persona("Noel", {'Direccion': 'Road 123', 'CP': '1222'}, {'Tel': '40401010'}, "no@el.com","second@mail.net")
    # agenda.listar_personas()
    # indice = agenda.buscar_persona('Carl')
    # print(indice)
    # agenda.datos_persona('Carl')
    # print(agenda.lista_personas)
    # agenda.guardar_shelve()
    # db = shelve.open('shelve_db_agenda')
    # print(len(db))
    # carl = db['Carl']  # se puede acceder por key a lo guardado con shelve
    # carl.print_persona()
    print("Ana esta en agenda?", agenda.buscar_persona("Ana"))
    # agenda.listar_personas()
    agenda.datos("Noel")
