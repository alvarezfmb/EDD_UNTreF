import csv

# CSV formato Fecha y Hora; Nombre; Obra Social; Codigo Paciente; Tipo Consulta / Ordenado por fecha y hora
# generar un archivo de texto que provea info para cada obra social
# para cada obra social, pacientes que se atendieron ordenados por fecha y hora, en que fecha
# y hora y cual es el tipo de consulta.
# Ademas, resumen total de pacientes para cada obra social.

# Fecha y Hora,Nombre,Obra Social,Cod Paciente,Tipo de consulta


def next_line(x):
    try:
        return next(x)
    except:
        return None


def datos_csv():
    dicc = {}
    file = open('obras_sociales.csv', 'r')
    next(file)  # salteo linea de titulos
    reader = csv.reader(file, delimiter=',')
    for line in reader:
        if line[2] not in dicc:  # si obra social no esta en dicc, la agrego con una lista como valor
            dicc[line[2]] = []
        dicc[line[2]].append((line[0], line[1], line[3], line[4]))  # agrego datos del paciente a la lista

    file.close()
    return dicc


def escribir_archivo(dicc):
    archivo = open('informe.txt', 'w')
    for k in dicc.keys():
        print(k, file=archivo)
        for paciente in dicc[k]:
            print(paciente)
            print('"', paciente[0], '",', paciente[1], paciente[2], paciente[3], file=archivo)
        print('Cant', len(dicc[k]), file=archivo)


if __name__ == '__main__':
    x = datos_csv()
    print(x)
    escribir_archivo(x)

