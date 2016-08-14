list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def sumatoria(list):
    total = 0
    for x in list:
        total += x
    return total


def promedio(list):
    return sumatoria(list) / len(list)


def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n - 1) * n


def menorIgualMayor(list, num):
    mayor = []
    menor = []
    igual = []
    for x in list:
        if x > num:
            mayor.append(x)
        elif x < num:
            menor.append(x)
        else:
            igual.append(x)
    return mayor, menor, igual


# x,y,z = menorIgualMayor(list,5)
# print(x,y,z)

def isPrime(n):
    if n < 1:
        return False

    if n == 1:
        return True

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def listaPrimos(list):
    listaSalida = []
    for x in list:
        if (isPrime(x)):
            listaSalida.append(x)
    return listaSalida
