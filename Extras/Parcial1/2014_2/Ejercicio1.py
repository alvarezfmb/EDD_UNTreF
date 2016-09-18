import csv
import pickle


# (a) Se tiene un archivo CSV de libros con columnas Título, Autor, Editorial, Año de publicación.
# Escribir una función para generar dos diccionarios uno de autores con contenido lista de termas
# (Título, Editorial, Año de publicación) y otro de editoriales con lista de ternas
# (Título, Autor, Año de publicación).
# (b) Escribir funciones Python para hacer persistentes estos diccionarios y para recuperarlos.

# 0_TITULO 1_AUTOR 2_EDITORIAL 3_ANIO


def leer_csv():
    dicc_autores = {}
    dicc_editoriales = {}
    file = open('libreria.csv', 'r')
    next(file)
    reader = csv.reader(file, delimiter=';')
    for line in reader:
        if line[1] not in dicc_autores:
            dicc_autores[line[1]] = []
        dicc_autores[line[1]].append((line[0], line[2], line[3]))
        if line[2] not in dicc_editoriales:
            dicc_editoriales[line[2]] = []
        dicc_editoriales[line[2]].append((line[0], line[1], line[3]))
    return dicc_autores, dicc_editoriales


def guardar(dicc1, dicc2):
    pickle.dump(dicc1, open('dicc1.p', 'wb'))
    pickle.dump(dicc2, open('dicc2.p', 'wb'))


def abrir():
    dicc1 = pickle.load(open('dicc1.p', 'rb'))
    dicc2 = pickle.load(open('dicc2.p', 'rb'))
    return dicc1, dicc2


if __name__ == '__main__':
    # a, b = leer_csv()
    # print(a)
    # print(b)
    # guardar(a, b)
    a, b = abrir()
    print(a)
    print(b)
