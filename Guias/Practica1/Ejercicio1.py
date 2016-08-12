# operaciones aritmeticas basicas

import math

def operaciones():
    print(2 ** 1024)
    print (1/3 + 1/5)

def formulaResolvente(a,b,c):
    root = math.sqrt((b ** 2) - 4 * a * c)
    positive = (-b +  root) / (2 * a)
    negative = (-b - root) / (2 * a)
    return positive,negative


operaciones()
print(formulaResolvente(1,-8,15))