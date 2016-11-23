import functools
import re

from lxml import etree
from datetime import datetime
from config import *
from getter_de_noticias import _crear_fecha
from inverted_index import InvertedIndex
import pickle
from exceptions import *


class GestorDeConsultas:
    def __init__(self):
        self.inverted_index = InvertedIndex()
        self.indice_inv_titulos, self.estructura_aux_titulos = pickle.load(open("indice_titulos.db", "rb")), \
                                                               pickle.load(open("auxiliar_titulos.db", "rb"))
        self.indice_inv_desc, self.estructura_aux_desc = pickle.load(open("indice_descripciones.db", "rb")), \
                                                         pickle.load(open("auxiliar_descripciones.db", "rb"))

    def buscar_palabra(self, nro_palabra, clave_bloque, consulta):
        indice = ''
        # clave_bloque es posicion en indice
        # nro palabra es posicion dentro del bloque
        if consulta == 'title':
            indice = self.indice_inv_titulos
        else:
            indice = self.indice_inv_desc
        salto = 0
        salto_acumulado = 0
        while nro_palabra > 1:
            salto = indice[int(salto_acumulado) + int(clave_bloque):int(clave_bloque) + int(salto_acumulado) + 2]
            salto_acumulado += int(salto) + 2
            nro_palabra -= 1
        longitud = indice[int(clave_bloque) + int(salto_acumulado): int(clave_bloque) + int(salto_acumulado) + 2]
        try:
            palabra = indice[
                      int(clave_bloque) + 2 + int(salto_acumulado): int(clave_bloque) + 2 + int(salto_acumulado) + int(
                          longitud)]
        except:
            print('long', longitud)
            print('clave', clave_bloque)
            print('salto', salto_acumulado)
        return palabra

    def palabras_mas_frecuentes(self, cantidad, consulta, medio=None, seccion=None):
        dicc = {}
        if consulta == 'title':
            estructura = self.estructura_aux_titulos
        else:
            estructura = self.estructura_aux_desc
        for clave, bloque in estructura.items():
            for nro_palabra, palabra in enumerate(bloque, start=1):
                palabra_str = self.buscar_palabra(nro_palabra, clave, consulta)
                if not medio and not seccion:
                    dicc[palabra_str] = len(bloque[nro_palabra - 1])
                else:
                    apariciones = 0
                    for aparicion in bloque[nro_palabra - 1]:
                        if medio and not seccion:
                            if str(aparicion)[0] == medio:
                                apariciones += 1
                        elif not medio and seccion:
                            if str(aparicion)[1] == seccion:
                                apariciones += 1
                        else:
                            if str(aparicion)[0] == medio and str(aparicion)[1] == seccion:
                                apariciones += 1
                    if apariciones != 0:
                        dicc[palabra_str] = apariciones
        lista_dicc = list(dicc.items())
        lista_dicc_sorted = sorted(lista_dicc, key=lambda x: x[1], reverse=True)
        return lista_dicc_sorted[:cantidad]

    def contador_xml(self, contador, medio, seccion, fecha_inicial, fecha_final):
        archivo = 'xml/' + medio + '-' + seccion + '.xml'
        arbol = etree.parse(archivo)
        lista_noticias = arbol.xpath("//item")
        fechas_publicacion = arbol.xpath("//item/pubDate")
        for i, noticia in enumerate(lista_noticias):
            fecha_noticia_str = fechas_publicacion[i].text
            fecha_noticia_parseada = _crear_fecha(fecha_noticia_str)
            if fecha_noticia_parseada <= fecha_final and fecha_noticia_parseada >= fecha_inicial:
                contador += 1
            if fecha_noticia_parseada < fecha_inicial:
                break
        return contador

    def noticias_por_fecha(self, fecha_inicial, fecha_final, medio_param=None, seccion_param=None):
        contador = 0
        for medio in diccionario:
            for seccion in diccionario[medio]:
                if not medio_param and not seccion_param:
                    contador = self.contador_xml(contador, medio, seccion, fecha_inicial, fecha_final)
                elif medio_param and not seccion_param:
                    if medio == claves_medios_invertido[medio_param]:
                        contador = self.contador_xml(contador, medio, seccion, fecha_inicial, fecha_final)
                elif seccion_param and not medio_param:
                    if seccion == claves_secciones_invertido[seccion_param]:
                        contador = self.contador_xml(contador, medio, seccion, fecha_inicial, fecha_final)
                else:
                    if medio == claves_medios_invertido[medio_param] and seccion == claves_secciones_invertido[
                        seccion_param]:
                        contador = self.contador_xml(contador, medio, seccion, fecha_inicial, fecha_final)
        return contador

    def ranking_categorias(self, fecha_inicial, fecha_final):
        lista = []
        for medio in lista_medios:
            for seccion in lista_secciones:
                cant = self.noticias_por_fecha(fecha_inicial, fecha_final, claves_medios[medio],
                                               claves_secciones[seccion])
                lista.append((medio, seccion, cant))
        lista_ordenada = sorted(lista, key=lambda x: x[2], reverse=True)
        return lista_ordenada

    def crear_date(self, anio, mes, dia, hora):
        date = datetime(int(anio), int(mes), int(dia), int(hora))
        return date

    def parsear_consulta_booleana(self, consulta_string):
        operadores = {'and', 'nand', 'or', 'nor'}
        aux = ""
        aux2 = ""
        lista_consulta = consulta_string.split()
        consulta_tokenizada = []  # Sin stem ni stop words quitadas
        lst_palabras = []
        operadores_consulta = []
        for palabra in lista_consulta:
            palabra = self.inverted_index.estandarizar_palabra(palabra)
            if palabra not in operadores:
                if palabra not in self.inverted_index.stop_words and len(palabra) >= 4:
                    aux += self.inverted_index.stemmer.stem(palabra) + " "
                aux2 += palabra + " "
            else:
                lst_palabras.append(aux.strip())
                consulta_tokenizada.append(aux2.strip())
                aux = ""
                aux2 = ""
                operadores_consulta.append(palabra)
        if len(operadores_consulta) == 0:
            raise OperadoresNoValidosError('No se ingresaron operadores booleanos')
        lst_palabras.append(aux.strip())
        consulta_tokenizada.append(aux2.strip())
        return lst_palabras, operadores_consulta, consulta_tokenizada

    def generar_sets_por_bloques(self, lst_palabras, consulta, consulta_tokenizada_original):
        lista_conjuntos = []
        if consulta == 'title':
            estructura = self.estructura_aux_titulos
            indice = self.indice_inv_titulos
        else:
            estructura = self.estructura_aux_desc
            indice = self.indice_inv_desc
        for item_stem, item_full in zip(lst_palabras, consulta_tokenizada_original):
            item_tokenizado = item_stem.split()
            item_full_tokenizado = item_full.split()
            sets_item = []
            for palabra in item_tokenizado:
                bloque, nro_palabra = self.busqueda_binaria(palabra, consulta)
                if bloque != -1 and nro_palabra != -1:
                    set_bloque = {posting for posting in estructura[bloque][nro_palabra - 1]}
                    sets_item.append(set_bloque)
            set_item_parcial = functools.reduce(lambda x, y: x & y, sets_item)
            set_item_final = set()
            if len(item_full_tokenizado) > 1:  # Si es un frase
                for aparicion in set_item_parcial:
                    medio = claves_medios_invertido[str(aparicion)[0]]
                    seccion = claves_secciones_invertido[str(aparicion)[1]]
                    id_noticia = int(str(aparicion)[2:])
                    documento = medio + "-" + seccion + ".xml"
                    arbol = etree.parse("xml/" + documento)
                    noticia = arbol.xpath("//item[@id='{0}']/{1}/text()".format(id_noticia, consulta))[0]
                    noticia_estandarizada = self.inverted_index.estandarizar_texto(noticia)
                    if re.findall(item_full, noticia_estandarizada):  # Si no matchea la frase entera
                        set_item_final.add(aparicion)
            else:
                set_item_final = set_item_parcial
            lista_conjuntos.append(set_item_final)
        return lista_conjuntos

    def get_universo(self, consulta):
        conjuto_salida = set()
        if consulta == 'title':
            universo = self.estructura_aux_titulos
        else:
            universo = self.estructura_aux_desc
        for bloque in universo:
            for palabra in universo[bloque]:
                for aparicion in palabra:
                    conjuto_salida.add(aparicion)
        return conjuto_salida

    def operar_sets(self, lista_conjuntos, lista_operadores, consulta):
        universo = self.get_universo(consulta)
        set_resultado = lista_conjuntos[0]  # set resultado es el primero
        for conjunto in lista_conjuntos[1:]:
            for operador in lista_operadores:
                if operador == 'and':
                    set_resultado = set_resultado & conjunto
                elif operador == 'nand':
                    nuevo_conjunto = universo - conjunto
                    set_resultado = set_resultado & nuevo_conjunto
                elif operador == 'or':
                    set_resultado = set_resultado | conjunto
                elif operador == 'nor':
                    nuevo_conjunto = universo - conjunto
                    set_resultado = set_resultado | nuevo_conjunto
        return set_resultado

    def consulta_booleana(self, consulta_bool, consulta, numero_apariciones):
        lst_palabras, lst_operadores, consulta_tokenizada = self.parsear_consulta_booleana(consulta_bool)
        lista_conjuntos = self.generar_sets_por_bloques(lst_palabras, consulta, consulta_tokenizada)
        final = list(self.operar_sets(lista_conjuntos, lst_operadores, consulta))
        noticias_a_mostrar = []
        for noticia in final[:int(numero_apariciones)]:
            medio = str(noticia)[0]
            seccion = str(noticia)[1]
            id_noticia = int(str(noticia)[2:])
            arbol = etree.parse(
                "xml/" + claves_medios_invertido[medio] + "-" + claves_secciones_invertido[seccion] + ".xml")
            titulo_noticia = arbol.xpath("//item[@id='{0}']/title/text()".format(id_noticia), enconding="utf8")
            descripcion_noticia = arbol.xpath("//item[@id='{0}']/description/text()".format(id_noticia),
                                              encoding="utf8")
            noticias_a_mostrar.append((titulo_noticia, descripcion_noticia))
        return noticias_a_mostrar

    def busqueda_binaria(self, palabra, consulta):
        nro_bloque = -1
        nro_palabra = -1
        if consulta == 'title':
            estructura = self.estructura_aux_titulos
            indice = self.indice_inv_titulos
        else:
            estructura = self.estructura_aux_desc
            indice = self.indice_inv_desc
        claves = list(estructura)
        claves_total = list(estructura)
        cant_bloques = len(claves)
        claves.sort()
        claves_total.sort()
        flag = True
        while len(claves) >= 1 and flag:
            medio_indice = claves[int(cant_bloques / 2)]
            long_palabra = int(indice[medio_indice:medio_indice + 2])
            primera_palabra = indice[medio_indice + 2:medio_indice + 2 + long_palabra]
            if primera_palabra > palabra:
                claves = claves[:claves.index(medio_indice)]
            elif primera_palabra < palabra:
                bloque = indice[medio_indice:claves_total[claves_total.index(medio_indice) + 1]]
                if bloque.find(palabra) != -1:
                    flag = False
                    nro_bloque = medio_indice
                    bloque_split = re.split(r"\d+", bloque)
                    nro_palabra = bloque_split.index(palabra)
                else:
                    if len(claves) == 1:
                        break
                    claves = claves[claves.index(medio_indice):]

            else:
                flag = False
                nro_bloque = medio_indice
                bloque = indice[medio_indice:claves_total[claves_total.index(medio_indice) + 1]]
                bloque_split = re.split(r"\d+", bloque)
                nro_palabra = bloque_split.index(palabra)
            cant_bloques = len(claves)
        return nro_bloque, nro_palabra

    def listar_medios(self):
        print('Seleccionar medio')
        for i, medio in enumerate(lista_medios, start=1):
            print(i, '-', medio)

    def listar_secciones(self):
        print('Seleccionar seccion')
        for i, seccion in enumerate(lista_secciones, start=1):
            print(i, '-', seccion)