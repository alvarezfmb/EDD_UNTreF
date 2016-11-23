from lxml import etree

'''Dado el documento 'recetario.xml' Escribir las siguientes consultas:'''

arbol = etree.parse("receta.xml")


#1) Todas las recetas en la categoría Pescado que tengan Vino blanco como ingrediente;
b1 = arbol.xpath("//receta[categoria='Pescado']/ingredientes[ingrediente='Vino blanco']/..")

# print(len(a))
# print(a[0].text)
# for x in a:
#     print(a)
#     for y in a:
#         print(y)
#         print(y.text)


# b2) Todas las recetas que lleven hasta 45 minutos (verificar que la unidad de tiempo sea minutos) de preparación;
b2 = arbol.xpath("//receta/informacion_general/tiempo[.<=45 and @unidad='minutos']/../..")


# todas las recetas que se puedan preparar con 1 besugo (verificar que la cant del ingrediente sea 1)
b3 = arbol.xpath("//receta/ingredientes/ingrediente[@cantidad = 1 and .='Besugo']/../..")
b3 = arbol.xpath("//receta/ingredientes/ingrediente[@cantidad = 1][.='Besugo']/../..")
b3 = arbol.xpath("//receta/ingredientes[ingrediente = 'Besugo' and ./ingrediente[@cantidad = 1]]/..")
b3 = arbol.xpath("//receta[categoria = 'Pescado' and ./ingredientes[ingrediente = 'Vino blanco']]")
b3 = arbol.xpath("receta//ingredientes[ingrediente = 'Besugo'][.@cantidad = 1]/..")
print(b3)
print(b3[0][0].text)

# # todos los textos de los pasos numero 1 de las recetas
# b4 = arbol.xpath("//preparacion/paso[@numero = '1']")
# for x in b4:
#     print(x.text)
#
# #4) Todos los textos de los pasos número 1 de todas las recetas.
# d = arbol.xpath("//receta/preparacion/paso[@numero='1']/text()")
# print(d)