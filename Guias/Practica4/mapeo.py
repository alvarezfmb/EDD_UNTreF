import gmplot  # https://github.com/vgm64/gmplot
import csv
import googlemaps
from Guias.Practica4.config import *
# Subsample: https://github.com/paulgb/subsample


class Mapping:
    def __init__(self, path='datos-abiertos-deptos.csv', ciudad='Buenos Aires'):
        self.path = path
        if ciudad.strip() == '':
            self.gmap = gmplot.GoogleMapPlotter(-34.6036844, -58.3815591, 12)
        else:
            self.gmap = gmplot.GoogleMapPlotter.from_geocode(ciudad)
        self.lista_lat = []
        self.lista_lng = []
        self.maps_client = googlemaps.Client(key=KEY)

    # tomo subsample de 2000 casos para construir heatmap de deptos en venta
    def heatmap_deptos(self):
        with open(self.path, errors='ignore') as csvfile:
            reader = csv.reader(csvfile, delimiter=";")
            reader.__next__()
            for row in reader:
                try:
                    aux = self.maps_client.geocode(row[-8])
                    # lat, lng = self.gmap.geocode(row[-8])
                    self.lista_lat.append(aux[0]['geometry']['location']['lat'])
                    self.lista_lng.append(aux[0]['geometry']['location']['lng'])
                    print(self.lista_lng,self.lista_lat)
                    print(row[-8])
                except IndexError:
                    print("Excepcion atrapada")
            self.gmap.heatmap(self.lista_lng, self.lista_lat, threshold=1, radius=75)
            # Threshold: https://en.wikipedia.org/wiki/Threshold_model
            self.gmap.draw('mymap.html')


if __name__ == '__main__':
    mapeo = Mapping()
    mapeo.heatmap_deptos()
