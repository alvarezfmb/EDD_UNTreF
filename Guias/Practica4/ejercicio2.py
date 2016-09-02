import csv
import sys
import natsort


class CSVBiciComunas:
    def __init__(self, path1='/Users/fmbalvarez/PycharmProjects/EDD_UNTreF/Guias/Practica4/bicicleterias.csv',
                 path2='/Users/fmbalvarez/PycharmProjects/EDD_UNTreF/Guias/Practica4/comunas.csv'):
        self.path1 = path1
        self.path2 = path2
        self.dicc_comunas = {}

    def leer_comunas(self):
        csv.field_size_limit(sys.maxsize)
        with open(self.path2, errors='ignore') as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            reader.__next__()
            for row in reader:
                comuna = "Comuna " + row[-1]
                self.dicc_comunas[comuna] = {}
                self.dicc_comunas[comuna]['Barrios'] = row[-4]
                self.dicc_comunas[comuna]['Bicicleterias'] = {}

    def leer_bicicleterias(self):
        with open(self.path1, errors='ignore') as csvfile:
            reader = csv.reader(csvfile, delimiter=";")
            reader.__next__()
            for row in reader:
                self.dicc_comunas[row[-1]]['Bicicleterias'][row[2]] = row[3]

    def listar(self):
        dicc_ordenado = natsort.humansorted(self.dicc_comunas.items())
        print(self.dicc_comunas)
        print("DICC ORDENADO", dicc_ordenado)
        for x in dicc_ordenado:
            print(x[0], ":", x[1]['Barrios'], "\n")
            sub_dicc = natsort.humansorted(x[1]['Bicicleterias'])
            for k in sub_dicc:
                print(k, ":", x[1]['Bicicleterias'][k])
            print("\n")


if __name__ == '__main__':
    bici = CSVBiciComunas()
    bici.leer_comunas()
    bici.leer_bicicleterias()
    bici.listar()
