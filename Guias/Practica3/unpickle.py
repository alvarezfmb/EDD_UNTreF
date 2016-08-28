import pickle


def abrir_pickle():
    with open('/Users/fmbalvarez/PycharmProjects/EDD_UNTreF/Guias/Practica3/agenda.p', 'rb') as handle:
        return pickle.load(handle)


def mostrar_agenda_pickle():
    ap = abrir_pickle()
    print(ap)


if __name__ == '__main__':
