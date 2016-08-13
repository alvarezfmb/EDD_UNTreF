# extraer palabra de un texto y guardarla en variable

def extractor(texto,palabraAExtraer):
    longitud = len(palabraAExtraer)
    posicion = texto.find(palabraAExtraer)
    if posicion < 0:
        return "No se encontro la palabra"
    else:
        extraccion = texto[posicion:(posicion + longitud)]
        return extraccion


t1 = "En Estructura de Datos usamos Python como lenguaje de programacion"
p1 = "usamos"

print(extractor(t1,p1))
print(p1)