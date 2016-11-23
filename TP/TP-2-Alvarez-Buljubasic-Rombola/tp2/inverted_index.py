# -*- coding: utf-8 -*-
import functools
import re
import unicodedata
import pickle

from time import sleep
from lxml import etree
from nltk import SnowballStemmer

from config import *


class InvertedIndex:
    def __init__(self):
        self.stemmer = SnowballStemmer("spanish")
        self.stop_words = self.crear_dicc_stopwords()
        self.contador_bloque = 0
        self.comienzo_bloque = 0
        self.lista_aux = [[], [], [], []]

    def crear_dicc_stopwords(self):
        '''
        Genera un diccionario a partir del archivo stopwords_es.txt para facilitar su posterior manejo
        '''
        stop_words = set()
        for line in open("stopwords_es.txt", "r", encoding="utf8"):
            palabra = line[0:-1]
            stop_words.add(palabra)
        return stop_words

    def indice_invertido_map(self, consulta):
        '''
        :param consulta: 'title' or 'description' (titulo o cuerpo de la noticia)
        :return: lista de pares (token, docId) ordenados alfabeticamente y por docId de todos los medios y secciones
        '''
        lista_total = []
        for medio in lista_medios:
            for seccion in lista_secciones:
                tree = etree.parse("xml/" + medio + "-" + seccion + ".xml")
                nodos = reversed(tree.xpath("//item/" + consulta))
                lista_map = list(map(self.lematizar_y_generar_posting, nodos))
                for x in lista_map:
                    if x:
                        lista_total += x
        return sorted(lista_total, key=lambda n: n[0])

    def reduce_indice_estructura_block(self, palabra1, palabra2):
        '''
        :param palabra1: par (indice_comprimido, estructura_auxiliar) actual
        :param palabra2: par (token, docId) que se va a agregar al indice
        :return: Indice que sale de agregar palabra2 al indice existente
        '''
        indice = palabra1[0]
        ultima_palabra = ""
        # Busco la ultima palabra del indice actual
        for char in range(len(indice) - 1, 0, -1):
            if indice[char].isdigit():
                ultima_palabra = indice[char + 1:]
                break
        # Si el indice esta vacio o la palabra a agregar es distinta que la ultima agregada
        if indice == '' or (indice != '' and ultima_palabra != palabra2[0]):
            self.lista_aux[self.contador_bloque].append(int(palabra2[1]))
            self.contador_bloque += 1
            indice += str(len(palabra2[0])).zfill(2) + palabra2[0]
            # Si termine un bloque, empiezo un bloque nuevo
            if self.contador_bloque == 4:
                lista = palabra1[1].setdefault(self.comienzo_bloque, [])
                lista += self.lista_aux
                self.contador_bloque = 0
                self.comienzo_bloque = len(indice)
                self.lista_aux = [[], [], [], []]
        # Si la palabra a agregar es igual a la ultima agregada, agrego una nueva aparicion en la posicion que corresponda
        else:
            self.lista_aux[self.contador_bloque - 1].append(int(palabra2[1]))
        return indice, palabra1[1]

    def generar_indice_invertido(self, consulta):
        '''
        :param consulta: 'title' or 'description' (titulo o cuerpo de la noticia)
        :return: par (indice_comprimido, estructura_auxiliar)
        '''
        lista_map = self.indice_invertido_map(consulta)
        indice, estructura_aux = functools.reduce(self.reduce_indice_estructura_block, lista_map, ('', {}))
        return indice, estructura_aux

    def lematizar_y_generar_posting(self, item):
        '''
        :param item: objeto que representa el cuerpo de una noticia (description) o un titulo (title)
        :return: lista de pares (token, docId) para un item determinado con sus tokens lematizados
        '''
        lista = []
        if item.text:
            for palabra in re.split(r"\W+|\s+", item.text):
                # for palabra in re.split(r"[^A-Za-z\d]+|\s+", item.text):
                if palabra not in self.stop_words and len(palabra) >= 4:
                    palabra_estandarizada = self.estandarizar_palabra(palabra)
                    if palabra_estandarizada != "":
                        palabra_stem = self.stemmer.stem(palabra_estandarizada)
                        posting_id = item.getparent().get('id')
                        nuevo_posting = item.getparent().getparent().find("medio").text + \
                                        item.getparent().getparent().find("seccion").text
                        nuevo_posting += posting_id.zfill(4)
                        lista.append((palabra_stem, nuevo_posting))
        if not lista:
            return None
        return lista

    def estandarizar_palabra(self, palabra):
        '''
        :param palabra
        :return: palabra sin tildes y convertida a minusculas
        '''
        palabra_salida = ''.join(c for c in unicodedata.normalize('NFD', palabra)
                                 if unicodedata.category(c) != 'Mn')
        palabra_salida = re.sub(r'\d+', '', palabra_salida)
        return palabra_salida.lower()

    def estandarizar_texto(self, texto):
        texto_salida = ''.join(c for c in unicodedata.normalize('NFD', texto)
                               if unicodedata.category(c) != 'Mn')
        texto_salida = re.sub(r'\d+|,|\.|\'|;', '', texto_salida)
        return texto_salida.lower()

    def contar_cantidad_noticias(self):
        '''
        :return: int (cantidad de noticias de todos los medios y secciones)
        '''
        noticias = 0
        for medio in diccionario:
            for seccion in diccionario[medio]:
                tree = etree.parse("xml/" + medio + "-" + seccion + ".xml")
                noticias += len(tree.xpath("//item"))
        return noticias

    def guardar_indice(self, indice, nombre_archivo):
        pickle.dump(indice, open(nombre_archivo, "wb"))
