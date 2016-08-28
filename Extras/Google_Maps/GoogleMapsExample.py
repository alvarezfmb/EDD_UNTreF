#! /usr/bin/env python
# coding: utf8

from Extras.Google_Maps.config import *
import googlemaps
from googlemaps import convert

if __name__ == '__main__':
    ciudad1 = 'Buenos Aires'
    ciudad2 = 'Santiago'
    ciudad3 = 'Bariloche'

    gmaps = googlemaps.Client(key=KEY)  # inicializa la aplicación para consultar
    # los mapas de google
    ruta1 = gmaps.distance_matrix(ciudad1, ciudad2)
    ruta1 = gmaps.distance_matrix(ciudad1, ciudad3, None, "es", None, "metric")
    ruta2 = gmaps.distance_matrix(ciudad2, ciudad3)
    ruta3 = gmaps.distance_matrix(ciudad3, ciudad1)

    # def geocode(client, address=None, components=None, bounds=None, region=None,
    #            language=None):

    geo = gmaps.geocode("Santiago", None, None, None, "es")
    print(geo)

    print("RUTA 1 ", ruta1)
    # def distance_matrix(client, origins, destinations,
    #                    mode=None, language=None, avoid=None, units=None,
    #                    departure_time=None, arrival_time=None, transit_mode=None,
    #                    transit_routing_preference=None, traffic_model=None):

    print("ruta1: ", ruta1, '\n\n')
    # print("ruta2: ", ruta2, '\n\n')
    # print("ruta3: ", ruta3, '\n\n')

    # d1 = ruta1['rows'][0]['elements'][0]['distance']['value']
    # t1 = ruta1['rows'][0]['elements'][0]['duration']['value']
    # dias1 = int(t1 / 24 / 60 / 60)
    # t1 = t1 - dias1 * 24 * 60 * 60
    # horas1 = int(t1 / 60 / 60)
    # t1 = t1 - horas1 * 60 * 60
    # min1 = int(t1 / 60)

    # print("Distancia ruta 1: {0:8.4f} km".format(d1 / 1000000))
    # print("Tiempo estimado: {0:2d} dias, {1:2d} horas, {2:2d} min".format(dias1, horas1, min1))
