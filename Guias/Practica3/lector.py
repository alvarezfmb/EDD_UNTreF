class Lector():
    def leer_teclado(self):
        try:
            txt = input('Decime algo: ')
        except EOFError:
            return None
        except KeyboardInterrupt:
            return None
        if txt.isspace():
            return None
        return txt


if __name__ == '__main__':
    lector = Lector()
    print(lector.leer_teclado())
