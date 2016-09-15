from Guias.Practica5.invertedindex import *

# convierto los textos en strings
intro = open("textos/Introduccion.txt", "r", encoding="utf8")
text_intro = "".join(intro.readlines())
intro.close()

bombadil = open("textos/Bombadil.txt", "r", encoding="utf8")
egidio = open("textos/Egidio.txt", "r", encoding="utf8")
niggle = open("textos/Niggle.txt", "r", encoding="utf8")
roverandom = open("textos/Roverandom.txt", "r", encoding="utf8")
wootton = open("textos/Wootton.txt", "r", encoding="utf8")

text_bombadil = "".join(bombadil.readlines())
text_egidio = "".join(egidio.readlines())
text_niggle = "".join(niggle.readlines())
text_roverandom = "".join(roverandom.readlines())
text_wootton = "".join(wootton.readlines())

bombadil.close()
egidio.close()
niggle.close()
roverandom.close()
wootton.close()

dicc_invertido = {}
documentos = {'intro': text_intro, "Bombadil": text_bombadil, "Egidio": text_egidio, "Niggle": text_niggle,
              "Roverandom": text_roverandom, "Wotton": text_wootton}

for doc_id, text in documentos.items():
    doc_index = inverted_index(text)  # crea indice invertido de cada uno de los textos
    inverted_index_add(dicc_invertido, doc_id, doc_index)

# for word, doc_locations in dicc_invertido.items():
#    print(word, doc_locations)

print('GANDALF', dicc_invertido['gandalf'])
print('PINTOR', dicc_invertido['pintor'])
