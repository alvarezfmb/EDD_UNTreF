# Una dirección MAC (de placa de red) es una dirección formada por 6 bloques hexadecimales de 2 dígitos cada uno,
# separados por : o por -
# (a) Escribir una expresión regular que acepte sólo direcciones MAC válidas. Solo debe aceptar
# direcciones que usan el mismo separador. Por ejemplo 00:1F:A1:cC:11:9e es válida pero no 00-1F:A1- cC:11:9e .
# (b) Escribir una expresión regular que acepta sólo direcciones MAC capicúas que se lean exactamente igual (por ejemplo
# debe aceptar 00:1F:2A:A2:F1:00 pero no 00:1F:2A:2A:1F:00).

import re


def validar(direccion_mac):
    return re.match(r'[0-9A-Fa-f]{2}([:-])(?:[0-9A-Fa-f]{2}\1){4}[0-9A-Fa-f]{2}', direccion_mac)

print(validar('00:1F:A1:cC:11:9e'))

# 00:1F:F1:00
# 12345 3 54321
def validar_capicua_2(direccion_mac):
    return re.match(r'([0-9A-Fa-f])([0-9A-Fa-f])([:-])([0-9A-Fa-f])([0-9A-Fa-f])\3\5\4\3\2\1', direccion_mac)
#                       1            2            3     4           5

x = validar_capicua_2('00:1F:F1:00')
print(x.string)

def validar_capicua_completo(direccion_mac):
    return re.match(
        r'([0-9A-Fa-f])([0-9A-Fa-f])([:-])([0-9A-Fa-f])([0-9A-Fa-f])\3([0-9A-Fa-f])([0-9A-Fa-f])\3\7\6\3\5\4\3\2\1',
        direccion_mac)

x = validar_capicua_completo('00:1F:2A:A2:F1:00')
print(x.string)