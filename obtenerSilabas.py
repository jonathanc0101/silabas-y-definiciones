from dataclasses import dataclass
import json
from syltippy import syllabize


def obtenerPalabrasQueContenganLasSilabas(silabas, palabras, maxSilabas=3):
    palabrasNew = []
    for palabra in palabras:
        if (len(palabra["silabas"]) < maxSilabas):

            dentroDelConjunto = True

            for silaba in palabra["silabas"]:
                dentroDelConjunto &= silaba in silabas        
            
            if (dentroDelConjunto):
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

        # obtenemos las palabras que se forman con estas silabas
        palabrasObtenidas = [first, second] + \
            obtenerPalabrasQueContenganLasSilabas(silabas, palabras)
        
        n=6
        ##solo añadimos los batches que tengan mas de n palabras
        if(len(palabrasObtenidas) > n):
            silabasNew = []

            for palabra in palabrasObtenidas:
                silabasNew += palabra["silabas"]

            batch = {"silabas": silabasNew, "palabras": palabrasObtenidas}
            batches.append(batch)

    palabrasJson = json.dumps({"batches": batches})
    with open("palabrasSilabas.json", "w") as fileSilabas:
        fileSilabas.write(palabrasJson)
