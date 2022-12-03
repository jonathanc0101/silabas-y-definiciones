from dataclasses import dataclass
import json
from syltippy import syllabize

def getBatch(elems,amount):
    batch=[]
    for i in range(0,amount):
        if(len(elems) > 0):
            batch.append(elems.pop())
    return batch,elems

def separarEnBatchesDe(palabras,tamBatch = 4):
    batches = []
    batchesProcesados = []
    while len(palabras) > 0:
        # vamos agarrando de a tamBatch las palabras
        cantPalabras = len(palabras)

        if(cantPalabras != 0):
            batchPalabrasActual, palabras = getBatch(palabras,tamBatch)
            batches.append(batchPalabrasActual)
    
    for batch in batches:
        silabasNew = []
        for palabra in batch:
            silabasNew.extend(palabra["silabas"])
        batchesProcesados.append({"silabas":silabasNew,"palabras":batch})
        

    return batchesProcesados


with open("palabrasNuevasJson.txt", "r") as Myfile:
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


    batches = separarEnBatchesDe(palabras,4)

    palabrasJson = json.dumps({"batches": batches})
    with open("palabrasSilabasLast.json", "w") as fileSilabas:
        fileSilabas.write(palabrasJson)
