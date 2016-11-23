import re

# 1. (a) Escribir una expresión regular para asegurarse que una determinada
# cadena contenga únicamente una fecha con formato yyyy-mm- dd entre 1900-01-
# 01 y 2099-12- 31. Tener cuidado de que no acepte fechas tales como 1900-00-
# 00. Los separadores usados pueden ser tanto '-' como '/'. (b) Asegurarse que
# el separador usado para separar el día del mes sea el mismo que el que
# separa el mes del año (es decir que no acepte 1900-01/01). (c) Embeber en
# Python y verificar que sea realmente una fecha válida.


def validar(fecha):
	return re.match(r'(?:19|20)[0-9]{2}([-/])(?:0[1-9]|1[0-2])\1(?:0[1-9]|1[0-9]|2[0-9]|3[0-1])', fecha)


x = validar('2099-12-30')
print(x.string)

# 2. (a) Escribir una expresión regular que acepta únicamente cadenas no vacías donde se alternan estrictamente letras
# a y b: acepta a; ab; aba; abab; b; ba; bab y rechaza abb; baa; abba
# (b) Escribir una expresión regular que acepte sólo cadenas binarias que contengan la subcadena 111.

s = 'abab'
def ej2a(s):
	return re.match(r'(?:\b(?:ab)+a*\b|\b(?:ba)+b*\b|\bb\b|\ba\b)', s)

x = ej2a(s)
print(x.string)

s = '0101010100000001110110010'
def ej2b(s):
	return re.match(r'(?:[0-1]*1{3}[0-1]*)', s)

x = ej2b(s)
print(x.string)

match_b = re.findall(r'\b[01]*1{3}[01]*\b', "holaa h10101111 010111101 111 919 01010111lalala 111010111100")
print(match_b)