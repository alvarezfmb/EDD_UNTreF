matriz1 = [[1,2],[3,4]]
matriz2 = [[4,5],[6,7]]

def sumarMatricesCuadradas(matriz1,matriz2):
    matrizResult = matriz1 # setea el tamanio de la matriz resultante
    i = 0
    for row in matriz2:
        j = 0 # lo defino aca porque necesito que vuelva a cero con cada nueva fila que itero
        for column in row:
            matrizResult[i][j] += column
            j += 1
        i += 1
    return matrizResult

def diagonalDeMatriz(matriz):
    resultado = []
    i = 0
    for row in matriz:
        resultado.append(row[i])
        i += 1
    return resultado

# otra manera, como en los apuntes

def diagonalFuncional(matriz):
    # diag es la matriz en la posicion fila = columna
    # for itera hasta tamanio de matriz
    diag = [matriz[i][i] for i in range(len(matriz))]
    return diag

def crearMatrizIdentidad(size):
    result = []
    # agrega filas de ceros al resultado con 1 en posicion = fila
    for i in range(size):
        temp = crearFilaDeCeros(size)
        temp[i] = 1
        result.append(temp)
    return result

def crearFilaDeCeros(size):
    aux = []
    for i in range(size):
        aux.append(0)
    return aux

def trasponer(matriz):
    result = matriz
    i = 0
    for row in matriz:
        j = 0
        for column in row:
            result[i][j] = matriz[j][i]
            j += 1
        i += 1
    return result

