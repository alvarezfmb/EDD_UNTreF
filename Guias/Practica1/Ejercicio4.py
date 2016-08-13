# conversor de grados Fahrenheit a grados Celsius

def conversorCelsiusToF(gradosC):
    return (((9/5) * gradosC) + 32)

# imprimir conversion de grados celcius de 0 a 120

def listaConvertida():
    for i in range(0,120,10):
        print("C: " + str(i) + " F: " + str(conversorCelsiusToF(i)))

listaConvertida()