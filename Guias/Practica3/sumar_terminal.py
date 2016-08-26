# Ejercicio 4 Escribir una funci´on sumar() que sume todos los n´umeros ingresados por teclado
# (usar leer teclado()) y que ignore todos los ingresos que no son n´umeros v´alidos. Debe mostrar
# un mensaje de error en casos de ingresos err´oneos y mostrar la suma acumulada hasta el
# momento si el ingreso es v´alido. La funci´on debe terminar cuando el usuario ingresa una l´ınea
# en blanco. Asegurarse que pueda sumar tanto enteros como float.

from Guias.Practica3.lector import Lector


def sumar():
    res = 0
    flag = True
    while flag:
        try:
            txt_num = input("Ingresa un numero a sumar: ")
        except:
            print("Error en lectura de consola")
        if txt_num.isspace():
            print("Suma finalizada: ", res)
            flag = False
        elif check_num(txt_num) is not None:
            res += check_num(txt_num)
            print("Resultado parcial: ", res)
        else:
            print("Por favor ingrese un numero ")
    return res


def check_num(s):
    try:
        return float(s)
    except ValueError:
        return None


if __name__ == '__main__':
    print(sumar())
