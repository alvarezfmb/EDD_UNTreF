# usando SnowballStemmer

# coding: utf8
import urllib.request
import urllib
# import Stemmer
from nltk.stem.snowball import SnowballStemmer
from Extras.TP_test.config import *
from xml.etree.ElementTree import parse


def leer_rss(url):
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as rss:
            datos = rss.read()
        return datos
    except:
        return None


def lematizar(palabra):
    stemmer = SnowballStemmer("spanish")
    return stemmer.stem(palabra)


if __name__ == "__main__":
    telam_ultimas = leer_rss(telam_rss_url["ultimas"])
    telam_politica = leer_rss(telam_rss_url["politica"])
    telam_sociedad = leer_rss(telam_rss_url["sociedad"])
    telam_mundo = leer_rss(telam_rss_url["mundo"])
    telam_economia = leer_rss(telam_rss_url["economia"])

    print(telam_ultimas)

    # parsear XML de feed RSS
    u = urllib.request.urlopen('http://www.telam.com.ar/rss2/ultimasnoticias.xml')
    doc = parse(u)

    dicc_noticias = {}
    for item in doc.iterfind('channel/item'):
        title = item.findtext('title')
        date = item.findtext('pubDate')
        link = item.findtext('link')

        dicc_noticias[title] = [date, link]

        print(title)
        print(date)
        print(link)

    print(dicc_noticias)

    dicc = {"establecimiento": lematizar("establecimiento"),
            "establecido": lematizar("establecido"),
            "establecer": lematizar("establecer"),
            "establo": lematizar("establo")}

    print(dicc)
