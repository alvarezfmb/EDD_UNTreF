# from Guias.Practica3.pickle import *

class Agenda:
    agenda = []

    def __init__(self):
        agenda = abrir_pickle()

    def buscar_persona(self, nombre):
        return nombre in agenda


if __name__ == '__main__':
    agenda = Agenda
    agenda.buscar_persona("juan")
