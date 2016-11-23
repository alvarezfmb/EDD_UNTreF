diccionario = {"telam": {"ultimas": "http://www.telam.com.ar/rss2/ultimasnoticias.xml",
                         "politica": "http://www.telam.com.ar/rss2/politica.xml",
                         "sociedad": "http://www.telam.com.ar/rss2/sociedad.xml",
                         "economia": "http://www.telam.com.ar/rss2/economia.xml",
                         "mundo": "http://www.telam.com.ar/rss2/internacional.xml"},
               "clarin": {"ultimas": "http://www.clarin.com/rss/lo-ultimo/",
                          "politica": "http://www.clarin.com/rss/politica/",
                          "sociedad": "http://www.clarin.com/rss/sociedad/",
                          "economia": "http://www.clarin.com/rss/ieco/",
                          "mundo": "http://www.clarin.com/rss/mundo/"},
               "la-voz": {"ultimas": "http://www.lavoz.com.ar/rss.xml",
                          "politica": "http://www.lavoz.com.ar/taxonomy/term/4/1/feed",
                          "sociedad": "http://www.lavoz.com.ar/taxonomy/term/6/1/feed",
                          "economia": "http://www.lavoz.com.ar/taxonomy/term/2/1/feed",
                          "mundo": "http://www.lavoz.com.ar/taxonomy/term/5/1/feed"},
               "mendoza-online": {"ultimas": "http://www.mdzol.com/files/rss/todoslostitulos.xml",
                                  "politica": "http://www.mdzol.com/files/rss/politica.xml",
                                  "sociedad": "http://www.mdzol.com/files/rss/sociedad.xml",
                                  "economia": "http://www.mdzol.com/files/rss/economia.xml",
                                  "mundo": "http://www.mdzol.com/files/rss/mundo.xml"},
               "el-litoral": {"ultimas": "http://www.ellitoral.com/rss/um.xml",
                              "politica": "http://www.ellitoral.com/rss/poli.xml",
                              "sociedad": "http://www.ellitoral.com/rss/suce.xml",
                              "economia": "http://www.ellitoral.com/rss/econ.xml",
                              "mundo": "http://www.ellitoral.com/rss/inte.xml"}
               }

lista_medios = ['clarin', 'el-litoral', 'la-voz', 'mendoza-online', 'telam']
lista_secciones = ['ultimas', 'politica', 'sociedad', 'economia', 'mundo']
claves_medios = {"clarin": "1", "el-litoral": "2", "la-voz": "3", "mendoza-online": "4", "telam": "5"}
claves_secciones = {"ultimas": "1", "politica": "2", "sociedad": "3", "economia": "4", "mundo": "5"}

claves_medios_invertido = {"1": "clarin", "2": "el-litoral", "3": "la-voz", "4": "mendoza-online", "5": "telam"}
claves_secciones_invertido = {"1": "ultimas", "2": "politica", "3": "sociedad", "4": "economia", "5": "mundo"}

meses = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11,
         "Dec": 12}
