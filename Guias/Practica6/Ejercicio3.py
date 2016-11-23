import functools


# def maxima_temp_anual(ruta):
#     # Map: lee cada linea, separa anio, calidad y temp. Si calidad es adecuada y el dato no es faltante genera
#     # una linea en txt con formato aaaa,ttt
#     lst_salida = []
#     with open(ruta, 'r') as arch:
#         lst_salida.append((map(lambda x: [x[:4], x[12:], x[8:12]], arch.readline())))
#     return lst_salida

def generar_txt_intermedio(line):
    file = open('intermedio.txt', 'w')
    anio = line[0:4]
    temp = line[9:12]
    calidad = line[12]
    if calidad == '1' or calidad == '2' and temp != '999':
        linea_nueva = anio + ',' + temp
        file.write(linea_nueva + '\n')
    file.close()


def map_intermedio():
    file = open('archivo.txt', 'r')
    lst_lineas = [x for x in file]
    mp = map(generar_txt_intermedio, lst_lineas)
    file.close()


if __name__ == '__main__':
    map_intermedio()
