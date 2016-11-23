from lxml import etree

tree = etree.parse('courses.xml')

# root = tree.getroot()
# print(root)

# encontrar todos los nodos titulo
b1 = tree.xpath('//Titulo')

# encontrar todos los apellidos de todos los directores de departamento
b2 = tree.xpath('//Departamento/Director//Apellido')
# con // al inicio no es necesario indicar desde nodo raiz

# materias con mas de 500 vacantes
b3 = tree.xpath('//Materia[@Vacantes > 500]/Titulo')
# vacantes es atributo de materia

# listar titulos de deptos que tienen como correlativa a "CS106B"
b4 = tree.xpath("//Materia/Correlativas[Corre = 'CS106B']/../../Titulo")
# /../../ subo dos niveles

# apellidos de los docentes que firman con segundo nombre
b5 = tree.xpath('//Docentes//Segundo_Nombre/../Apellido')

# apellidos de docentes que tienen materias con vacantes >= 100
b6 = tree.xpath('//Materia[@Vacantes >= 100]/Docentes//Apellido')

b7 = tree.xpath('//Materia//Titulo[@atri = 1]/..')

b7 = tree.xpath('//Materia[@cat = "x" and ./Titulo[@atri = 1]]')

b7 = tree.xpath('//Materia[./num > 10]/@Numero')

# num de materia de materias con mas de n num
b7 = tree.xpath('//Materia[./num > 10]/../@Codigo')

#nombre de materias con mas de mil vacantes
b7 = tree.xpath('//Materia[@Vacantes > 1000]/@Numero')



print(b7)
for x in b7:
    print(x.text)

