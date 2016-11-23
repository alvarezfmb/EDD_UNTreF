# Escribir un programa Python que maneje expresiones regulares y que encuentre y reemplace dentro de un texto todos
# los nombres de usuarios de twitter por la palabra USER (los usuarios de twitter comienzan con @ seguido de letras y
# números, por ejemplo: @usuario21). Se debe tener cuidado de no atrapar y reemplazar direcciones de correo
# electrónico con la forma usuario@dominio.

import re


def ej2(string):
    return re.sub(r'(?:\B@\w*)', 'USER', string)

x = ej2('@23sdsd2 hola@nose 1@unacuenta this@mail.net')
print(x)


string = '@23sdsd2 hola@nose 1@unacuenta this@mail.net'
salida = re.sub(r"(?<!\w)@\w+", "USER", string)
print(salida)

