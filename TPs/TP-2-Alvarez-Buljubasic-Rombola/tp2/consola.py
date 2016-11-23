from gestor_de_consultas import GestorDeConsultas
from exceptions import *


class Consola:
    def __init__(self):
        self.gestor = GestorDeConsultas()

    def principal(self):
        while True:
            print("MENU PRINCIPAL\n")
            print("1- Ranking de palabras")
            print("2- Categorias mas activas en un rango de fecha")
            print("3- Filtrar noticias por fecha y hora")
            print("4- Consulta booleana")
            print("5- Salir del programa")
            opcion = input("Ingrese la opción que desea\n")
            if opcion == "1":
                self.ranking_de_palabras()
            elif opcion == "2":
                self.categorias_mas_activas()
            elif opcion == "3":
                self.filtrar_noticias()
            elif opcion == "4":
                self.consulta_booleana()
            elif opcion == "5":
                self.salir()
            else:
                print("La opcion ingresada no es valida\n\n")

    def ranking_de_palabras(self):
        self.gestor.listar_medios()
        medio = input("\nIngrese numero de medio a buscar(opcional)\n")
        self.gestor.listar_secciones()
        seccion = input("Ingrese numero de seccion a buscar (opcional)\n")
        cant_a_mostrar = input("Ingrese cantidad de palabras que desea mostrar\n")
        if medio:
            if int(medio) <= 0 or int(medio) >= 6:
                print('Revisar opciones ingresadas')
                self.ranking_de_palabras()
        if seccion:
            if int(seccion) <= 0 or int(seccion) >= 6:
                print('Revisar opciones ingresadas')
                self.ranking_de_palabras()
        if not cant_a_mostrar or int(cant_a_mostrar) <= 0:
            print('Revisar cantidad a mostrar ingresada')
            self.ranking_de_palabras()
        if medio == "":
            medio = None
        if seccion == "":
            seccion = None
        print("¿Donde desea buscar?")
        print("title -- Titulos")
        print("description -- Descripciones")
        consulta = input()
        ranking = self.gestor.palabras_mas_frecuentes(int(cant_a_mostrar), consulta, medio, seccion)
        for i, tupla in enumerate(ranking, start=1):
            print(i, '-', tupla[0], '->', tupla[1], 'apariciones')

    def categorias_mas_activas(self):
        fecha_inicial_parseada, fecha_final_parseada = self.parsear_fecha()
        ranking = self.gestor.ranking_categorias(fecha_inicial_parseada, fecha_final_parseada)
        for i, tupla in enumerate(ranking, start=1):
            print(i, '-', tupla[0], tupla[1], '->', tupla[2])

    def parsear_fecha(self):
        fecha_inicial = input("ingrese fecha inicial en formato aaaa,mm,dd,hh\n")
        fecha_final = input("ingrese fecha final en formato aaaa,mm,dd,hh\n")
        fecha_inicial = fecha_inicial.split(",")
        fecha_final = fecha_final.split(",")
        try:
            fecha_inicial_parseada = self.gestor.crear_date(fecha_inicial[0], fecha_inicial[1], fecha_inicial[2],
                                                            fecha_inicial[3])
            fecha_final_parseada = self.gestor.crear_date(fecha_final[0], fecha_final[1], fecha_final[2],
                                                          fecha_final[3])
        except (TypeError, ValueError, IndexError):
            print("Revisar formato de fechas ingresadas")
            self.principal()
        return fecha_inicial_parseada, fecha_final_parseada

    def filtrar_noticias(self):
        fecha_inicial_parseada, fecha_final_parseada = self.parsear_fecha()
        self.gestor.listar_medios()
        medio = input("\nIngrese numero de medio a buscar(opcional)\n")
        self.gestor.listar_secciones()
        seccion = input("Ingrese numero de seccion a buscar (opcional)\n")
        if medio:
            if int(medio) <= 0 or int(medio) >= 6:
                print('Revisar opciones ingresadas')
                self.filtrar_noticias()
        if seccion:
            if int(seccion) <= 0 or int(seccion) >= 6:
                print('Revisar opciones ingresadas')
                self.filtrar_noticias()
        print(self.gestor.noticias_por_fecha(fecha_inicial_parseada, fecha_final_parseada, medio, seccion))

    def consulta_booleana(self):
        consulta_bool = input('Ingrese consulta booleana (operadores validos: AND, OR, NAND, NOR\n')
        print("¿Donde desea buscar?")
        print("title -- Titulos")
        print("description -- Descripciones")
        consulta = input()
        numero_apariciones = input('Ingrese numero de apariciones a mostrar\n')
        if not numero_apariciones or int(numero_apariciones) <= 0 or not consulta_bool or not consulta:
            print('Revisar valores ingresados')
            self.consulta_booleana()
        try:
            noticias = self.gestor.consulta_booleana(consulta_bool, consulta, numero_apariciones)
        except OperadoresNoValidosError:
            print('Revisar la consulta booleana')
            self.consulta_booleana()
        for x in noticias:
            print(x[0][0])
            print(x[1][0], '\n')

    def salir(self):
        exit()


if __name__ == '__main__':
    c = Consola()
    c.principal()
