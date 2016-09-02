import json
import pickle


class DataHolder():
    def __init__(self, nombre, dato):
        self.nombre = nombre
        self.dato = dato

    def __str__(self):
        return "nombre: " + self.nombre + " dato: " + self.dato


if __name__ == '__main__':
    data1 = DataHolder("A", 1)
    data2 = DataHolder("B", 2)
    dicc2 = {'#1': data1, '#2': data2}

    # pickle
    with open('data.p', 'wb') as fp:
        pickle.dump(dicc2, fp)
    with open('data.p', 'rb') as fp:
        data = pickle.load(fp)
    print(data)
    for x in data.items():
        print("Pickle:", x[1].__dict__)

    # json
    # funciona con todos estos tipos de datos
    dicc = {'A': 1, 'B': 2}
    s = "hola, ke ase"
    n = [4, 1, 5, 2]
    bool = True
    # guardo en JSON
    with open('data.json', 'w') as fp:
        json.dump(bool, fp, sort_keys=True)  # puedo serializar solo los objetos listados en los docs,
        # si no modifico clase JSONEncoder
    # leo de JSON
    with open('data.json', 'r') as fp:
        data = json.load(fp)
    print(data)
    # puedo guardar los datos de un objeto si uso el metodo __dict__
    with open('data.json', 'w') as fp:
        json.dump(data1.__dict__, fp, sort_keys=True)
    with open('data.json', 'r') as fp:
        data = json.load(fp)
    print(data)
    # loop for para recorrer items de diccionario
    for x in dicc2.items():
        print(x[1].__dict__)
        # guarda los datos del ultimo objeto en forma de diccionario (no concatena)
        with open('data.json', 'w') as fp:
            json.dump(x[1].__dict__, fp)
