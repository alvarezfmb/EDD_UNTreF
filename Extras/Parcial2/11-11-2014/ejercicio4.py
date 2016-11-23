# 4. Se tienen datos de temperaturas en un archivo .txt con el siguiente formato y se quiere calcular la temperatura
# máxima de cada año.
# Formato:
# Columnas 1 a 4: año; Columnas 5-6: mes; Columnas 7-8: día; Columna 9: signo de la temperatura (+ / -); Columnas 10
# a 12: temperatura * 10 (por ejemplo 346 se lee como 34.6 y 999 significa dato faltante); Columna 13: Calidad del dato
# (si la calidad no es 1 o 2, el dato no sirve).
# (a) Explicar en qué consiste el esquema Map/Reduce.
# (b) Escribir en Python dos funciones Map y Reduce con las siguientes especificaciones:
# Map:
# Lee cada línea de texto, separa año, temperatura y calidad y si la calidad es la adecuada y el dato no es faltante genera
# un línea de archivo de texto intermedio de la forma aaaa,ttt.
# Reduce:
# Lee el archivo de texto intermedio y produce el resultado deseado: año, máxima temperatura de cada año.

def mapper(txt):
    txt = open(txt, 'r')
    lst_intermedia = []
    file = open('intermedio.txt', 'w')
    for line in txt:
        anio = line[0:4]
        temp = int(line[8:12])
        calidad = int(line[12:])
        if calidad > 0 and calidad <=2 and temp != 999:
            file.write(anio + ',' + str(temp) + '\n')
    file.close()

def reducer():
    dicc = {}
    file = open('intermedio.txt', 'r')
    for line in file:
        aux = line.split(',')
        if line[0:4] not in dicc:
            dicc[aux[0]] = []
        dicc[line[0:4]].append(int(aux[1]))
    # for x in dicc.items():
    #     sorted(x[1])
    # print(dicc)
    file.close()
    file = open('final.txt', 'w')
    for x in dicc.items():
        file.write(str(x[0]) + ',' + str(max(x[1])) + '\n')


if __name__ == '__main__':
    mapper('archivo.txt')
    x = reducer()
    print(x)