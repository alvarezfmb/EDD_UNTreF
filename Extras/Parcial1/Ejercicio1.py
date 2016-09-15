import csv


# Se tiene un archivo CSV con columnas Padrón, Código de Materia, Tipo de Parcial, Nota, ordenado por
# Padrón, Código de Materia (Tipo de Parcial puede tomar los valores “P1”, “P2”, “R1”, “R2”).
#
# Escribir una función en Python para generar un diccionario con clave Padrón y cuyo contenido sea una lista de las
# materias regularizadas​ por cada alumno
#
# (las materias se regularizan cuando la nota máxima entre “P1” y “R1” es >=4 y lo mismo para el máximo entre “P2” y
# “R2”. Es posible que alguna de esos tipos de examen falte en la lista: si se rindió “R1” pero no “P1” y la nota
# de “R1” fue 6 se considera que la nota del primer  parcial es un 6, si no se rindió ni “P1” ni “R1” la nota para
# el primer parcial es 0).


def leer_csv():
    dicc = {}
    file = open('materias_parcial.csv', 'r')
    reader = csv.reader(file, delimiter=';')
    reader.__next__()
    for row in reader:
        if row[0] not in dicc:
            dicc[row[0]] = {}  # dicc con codigos de materias
        if row[1] not in dicc[row[0]]:
            dicc[row[0]][row[1]] = {'P1': 0, 'P2': 0, 'R1': 0, 'R2': 0}  # dicc con notas
        dicc[row[0]][row[1]][row[2]] = float(row[3])
    return dicc


def lista_de_regularizadas(dicc):
    dicc_salida = {}
    for alumno, materia in dicc.items():
        if alumno not in dicc_salida:
            dicc_salida[alumno] = []
        if materia not in dicc_salida[alumno]:
            for x in materia.items():
                if max(x[1]['P1'], x[1]['R1']) >= 4 and max(x[1]['P2'], x[1]['R2']) >= 4:
                    dicc_salida[alumno].append(x[0])
    return dicc_salida


if __name__ == '__main__':
    dicc = leer_csv()
    print('DICC', dicc)
    salida = lista_de_regularizadas(dicc)
    print('SALIDA', salida)
