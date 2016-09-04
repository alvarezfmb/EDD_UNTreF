import csv
import natsort
import gmplot


class BicicleteriasCSV:
    def __init__(self, path='/Users/fmbalvarez/PycharmProjects/EDD_UNTreF/Guias/Practica4/bicicleterias.csv'):
        self.path = path
        self.dicc_comunas = {}
        self.lista_lat = []
        self.lista_lng = []
        self.lista_val = []
        self.gmap = gmplot.GoogleMapPlotter(-34.6036844, -58.3815591, 12)

    def leer_csv(self):
        with open(self.path, errors='ignore') as csvfile:  # ignora posibles errores de encoding
            reader = csv.reader(csvfile, delimiter=";")
            reader.__next__()  # para ignorar primer linea del csv
            # csv separa items de columnas con punto y coma, si delimiter se setea asi devuelve cada
            # columna como un item separado de la lista
            for row in reader:
                if row[-1] not in self.dicc_comunas:
                    self.dicc_comunas[row[-1]] = {}
                    self.dicc_comunas[row[-1]]['Barrios'] = {}
                    self.dicc_comunas[row[-1]]['Total comuna'] = 1
                else:
                    self.dicc_comunas[row[-1]]['Total comuna'] += 1
                if row[-2] not in self.dicc_comunas[row[-1]]['Barrios']:
                    self.dicc_comunas[row[-1]]['Barrios'][row[-2]] = 1
                else:
                    self.dicc_comunas[row[-1]]['Barrios'][row[-2]] += 1

    def humansort_dicc(self, dicc):
        dicc_ordenado = natsort.humansorted(dicc)  # libreria para human sorting de keys del dicc
        return dicc_ordenado

    def mapear_bicicletas(self):
        with open(self.path, errors='ignore') as csvfile:
            reader = csv.reader(csvfile, delimiter=";")
            reader.__next__()
            for line in reader:
                string = ''.join(c for c in line[0] if c not in 'POINT()')
                str_list = string.split(" ")
                tupla_lat_lng = (float(str_list[-2]), float(str_list[-1]))
                self.lista_val.append(tupla_lat_lng)
            for x in self.lista_val:
                self.gmap.marker(x[1], x[0])
            self.gmap.draw('mapeo-bicicleterias.html')

    def listar(self):
        dicc = self.humansort_dicc(self.dicc_comunas.items())
        for x in dicc:
            print(x[0], ":", "\n")
            sub_dicc = self.humansort_dicc(x[1]['Barrios'].items())
            for k, v in sub_dicc:
                print(k, ":", v)
            print("Total comuna: ", x[1]['Total comuna'])
            print("\n")


if __name__ == '__main__':
    b = BicicleteriasCSV()
    # b.leer_csv()
    # b.listar()
    b.mapear_bicicletas()
