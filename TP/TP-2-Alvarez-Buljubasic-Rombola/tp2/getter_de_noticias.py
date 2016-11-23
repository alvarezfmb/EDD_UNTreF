from lxml import etree
from config import *
from datetime import datetime
import os
from contextlib import contextmanager
import schedule


def _crear_xml(nombre_medio, nombre_seccion, link):
    ''' Crea archivo XML inicial. Recibe parametros desde diccionario de config '''
    arbol = etree.parse(link)
    folder = os.getcwd() + '/xml'
    if not os.path.exists(folder):
        os.makedirs(folder)
    with _cd(folder):
        arbol.write(nombre_medio + "-" + nombre_seccion + ".xml", encoding="utf8")


def enumerar_xml(nombre_medio, nombre_seccion):
    '''
    Agrega a un archivo xml dado, etiquetas que identifican el medio y la seccion
    '''
    with _cd(os.getcwd() + '/xml'):
        arbol = etree.parse(nombre_medio + "-" + nombre_seccion + ".xml")
        root = arbol.getroot()
        r = root.find("channel/description")
        seccion = etree.Element("seccion")
        seccion.text = claves_secciones[nombre_seccion]
        r.addnext(seccion)
        medio = etree.Element("medio")
        medio.text = claves_medios[nombre_medio]
        r.addnext(medio)
        arbol.write(nombre_medio + "-" + nombre_seccion + ".xml", encoding="utf8")


def _obtener_updates_xml(medio, seccion):
    '''
    Descarga las nuevas noticias y las agrega al principio de cada xml
    '''
    with _cd(os.getcwd() + '/xml'):
        try:
            arbol_local = etree.parse(medio + '-' + seccion + '.xml')
            arbol_internet = etree.parse(diccionario[medio][seccion])
        except:
            print("No se pudo leer", diccionario[medio][seccion])
        else:
            aux_fecha_ultima_noticia_texto = arbol_local.xpath("//item/pubDate")[0].text
            fecha_ult_noticia = _crear_fecha(aux_fecha_ultima_noticia_texto)
            lista_noticias_internet = arbol_internet.xpath("//item")
            prox = lista_noticias_internet[0].find("pubDate").text
            fecha_prox = _crear_fecha(prox)
            root_local = arbol_local.getroot()
            i = 0
            while fecha_ult_noticia < fecha_prox and i < len(lista_noticias_internet) - 1:
                item = root_local.findall("channel/item")[i]
                if i == 0:
                    item.addprevious(lista_noticias_internet[i])
                    agregar_despues = root_local.findall("channel/item")[0]
                else:
                    if i == 1:
                        agregar_despues.addnext(lista_noticias_internet[i])
                    else:
                        item.addnext(lista_noticias_internet[i])
                i += 1
                prox = lista_noticias_internet[i].find("pubDate").text
                fecha_prox = _crear_fecha(prox)
            arbol_local.write(medio + '-' + seccion + '.xml', encoding="utf8")


def _crear_fecha(elemento):
    dia = int(elemento[5:7])
    mes = meses[elemento[8:11]]
    anio = int(elemento[12:16])
    horas = int(elemento[17:19])
    minutos = int(elemento[20:22])
    fecha_parseada = datetime(anio, mes, dia, horas, minutos)
    return fecha_parseada


def obtener_noticas():
    ''' Crea XML de todas los medios y secciones del diccionario '''
    for medio in diccionario:
        for seccion in diccionario[medio]:
            _crear_xml(medio, seccion, diccionario[medio][seccion])


def _actualizar_noticias():
    ''' Actualiza noticias de todos los feeds del diccionario '''
    for medio in diccionario:
        for seccion in diccionario[medio]:
            _obtener_updates_xml(medio, seccion)
            etiquetar_xml(medio, seccion)
            enumerar_xml(medio, seccion)


def actualizar_cada_n_minutos(n):
    schedule.every(n).minutes.do(_actualizar_noticias)


def etiquetar_xml(medio, seccion):
    '''
    Identifica cada noticia de un xml dado con una id unica
    '''
    with _cd(os.getcwd() + '/xml'):
        tree = etree.parse(medio + "-" + seccion + ".xml")
        root = tree.getroot()
        cant_items = len(tree.xpath("//item"))
        for noticia in root.iter("item"):
            noticia.set("id", str(cant_items))
            cant_items -= 1
            tree.write(medio + "-" + seccion + ".xml", encoding="utf-8")


@contextmanager
def _cd(newdir):
    ''' Cambia el contexto de ejecucion para escribir los XML en una sub-carpeta '''
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)


if __name__ == '__main__':
    _actualizar_noticias()
