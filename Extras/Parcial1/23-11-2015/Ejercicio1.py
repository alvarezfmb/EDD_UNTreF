import csv


# Se tienen dos archivos CSV uno con columnas Código de Materia, Padrón, Nota, ordenado por Código de
# Materia, y otro con Código de Materia, Departamento, ordenado por Código de Materia. Escribir una función
# en Python para generar un diccionario con clave Departamento y cuyo valor sea la cantidad de alumnos que
# aprobaron materias de ese Departamento (las materias se aprueban con nota mayor o igual a 4).

# CODIGO_MAT PADRON NOTA <-- csv_padron
# CODIGO_MAT DEPARTAMENTO <-- csv_depto
# --> {'Departamento': cant_aprobados}


def leer_csv():  # version beta, mejor el de abajo
    dicc = {}
    dicc_materias = {}
    file = open('csv_padron.csv', 'r')
    next(file)
    reader = csv.reader(file, delimiter=';')
    for line in reader:
        if line[0] not in dicc_materias:
            dicc_materias[line[0]] = 0  # necesito agregarla aunque no tenga aprobados
        if float(line[2]) >= 4:
            dicc_materias[line[0]] += 1  # {'Cod_Materia': cant_aprobados}
    file = open('csv_depto.csv', 'r')
    next(file)
    reader = csv.reader(file, delimiter=';')
    print(dicc_materias)
    for line in reader:
        dicc[line[1]] = dicc.get(line[1], 0) + dicc_materias[line[0]]
    return dicc


def leer():  # tip to Guid1OS
    dicc_depto = {}  # {'Depto': [(set materias), (set padrones)]}
    file = open('csv_depto.csv', 'r')
    next(file)
    reader = csv.reader(file, delimiter=';')
    for line in reader:
        if line[1] not in dicc_depto:
            dicc_depto[line[1]] = []
            dicc_depto[line[1]].append(set())
            dicc_depto[line[1]].append(set())
        dicc_depto[line[1]][0].add(line[0])
    file = open('csv_padron.csv', 'r')
    next(file)
    reader = csv.reader(file, delimiter=';')
    for line in reader:
        if float(line[2]) >= 4:
            for depto in dicc_depto.items():
                if line[0] in depto[1][0]:
                    depto[1][1].add(line[1])
    print(dicc_depto)
    for k, v in dicc_depto.items():
        dicc_depto[k] = len(v[1])
    return dicc_depto


# def nuevo_leer():  # tip to Guid1OS
#     dicc = {}
#     dicc_padron = {}
#     file = open('csv_padron.csv', 'r')
#     next(file)
#     reader = csv.reader(file, delimiter=';')
#     for line in reader:  # {'Padron': codigo de materias que aprobo}
#         if line[1] not in dicc_padron:
#             dicc_padron[line[1]] = []
#         if float(line[2]) >= 4:
#             dicc_padron[line[0]].append(line[0])
#     file = open('csv_depto.csv', 'r')
#     next(file)
#     reader = csv.reader(file, delimiter=';')
#     for line in reader:
#         if line[1] not in dicc:
#             dicc[line[1]] = 0
#     for padron, lst_materias in dicc_padron.items():


# def leer_aprovechando_ordenamiento():
#     dicc = {}
#     file = open('csv_padron.csv', 'r')
#     next(file)
#     reader = csv.reader(file, delimiter=';')
#     file2 = open('csv_depto.csv', 'r')
#     next(file2)
#     reader2 = csv.reader(file, delimiter=';')
#     for line in reader2:
#         dicc[line[1]] = 0  # {'Departamento': }
#         while


if __name__ == '__main__':
    dicc = leer()
    print(dicc)
