from dataclasses import dataclass
import json
from syltippy import syllabize


def obtenerPalabrasQueContenganLasSilabas(silabas, palabras, maxSilabas=2):
    palabrasNew = []
    for palabra in palabras:
        cantSilabas = len(palabra["silabas"])
        

        if (cantSilabas <= maxSilabas):
            silabasCopiadas = palabra["silabas"].copy()

            scoresSilabas = dict(zip(palabra["silabas"],[0 for x in silabasCopiadas]))

            while(len(silabasCopiadas) > 0):
                scoresSilabas[silabasCopiadas.pop(0)] += 1

            silabasAux = set(palabra["silabas"])

            interseccion = silabas.intersection(silabasAux)

            score = 0

            for sil in interseccion:
                score += scoresSilabas[sil]
                    

            if (score >= 2):
                palabrasNew.append(palabra)

    return palabrasNew


with open("palabrasJson.txt", "r") as Myfile:
    data = json.load(Myfile)

    palabras = []
    batches = []

    for palabra in data:
        syllabes, stress = syllabize(palabra)
        if (len(syllabes) > 1):
            p = {}
            p["silabas"] = syllabes
            p["palabra"] = palabra
            palabras.append(p)

    while (len(palabras) > 0):
        # vamos agarrando de a dos palabras
        first, second = palabras.pop(0), palabras.pop(0)
        # les sacamos las silabas y hacemos un set
        silabas = set(first["silabas"] + second["silabas"])

        palabrasObtenidas = [first, second] + \
            obtenerPalabrasQueContenganLasSilabas(silabas, palabras)
        silabasNew = []

        for palabra in palabrasObtenidas:
            silabasNew += palabra["silabas"]

        silabasNew = list(set(silabasNew))

        batch = {"silabas": silabasNew, "palabras": palabrasObtenidas}
        batches.append(batch)

    palabrasJson = json.dumps({"batches": batches})
    with open("palabrasSilabas.json", "w") as fileSilabas:
        fileSilabas.write(palabrasJson)
