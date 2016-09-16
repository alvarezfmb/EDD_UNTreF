import csv


# Se tienen dos archivos CSV uno con columnas Código de Materia, Padrón, Nota, ordenado por Código de
# Materia, y otro con Código de Materia, Departamento, ordenado por Código de Materia. Escribir una función
# en Python para generar un diccionario con clave Departamento y cuyo valor sea la cantidad de alumnos que
# aprobaron materias de ese Departamento (las materias se aprueban con nota mayor o igual a 4).

# CODIGO_MAT PADRON NOTA <-- csv_padron
# CODIGO_MAT DEPARTAMENTO <-- csv_depto
# --> {'Departamento': cant_aprobados}


def leer_csv():
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


if __name__ == '__main__':
    dicc = leer_csv()
    print(dicc)
