import pickle


def agregar_a_agenda(nombre, domicilio, tel, *emails):
    datos = (nombre, {'Tel': tel, 'Email': [], 'Domicilio': domicilio})
    for i in emails:
        datos[1]['Email'].append(i)
    agenda_picke = abrir_pickle()
    agenda_picke.append(datos)
    conservar_en_pickle(agenda_picke)


def conservar_en_pickle(data):
    # with cierra el archivo luego de que se ejecute lo de adentro, sin importar si hay excepcion
    with open('/Users/fmbalvarez/PycharmProjects/EDD_UNTreF/Guias/Practica3/agenda.p', 'wb') as handle:
        pickle.dump(data, handle)


def abrir_pickle():
    with open('/Users/fmbalvarez/PycharmProjects/EDD_UNTreF/Guias/Practica3/agenda.p', 'rb') as handle:
        return pickle.load(handle)


def mostrar_agenda_pickle():
    ap = abrir_pickle()
    print(ap)


if __name__ == '__main__':
    # agregar_a_agenda("Carl", {'Direccion': "Fake 123",'CP': 1678}, "40402020""pepi@gmail.com", "sds@gm.com","otro@mas.org.uy")
    # agenda = abrir_picke()
    # print(agenda)
    # conservar_en_picle(agenda)
    # agregar_a_agenda("Ana",{'Direccion': "San Martin 2100", 'Piso': 9},"1523343202","ana@banana.net","ana@simmetry.com")
    mostrar_agenda_pickle()
