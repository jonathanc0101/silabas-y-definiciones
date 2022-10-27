from dataclasses import dataclass
import json
from syltippy import syllabize


with open("palabrasJson.txt", "r") as Myfile:
    data = json.load(Myfile)
    
    palabras = []
    
    
    for palabra in data:
        syllabes, stress = syllabize(palabra)
        p = {}
        p["silabas"] = syllabes
        p["palabra"] = palabra
        palabras.append(p)

    palabrasJson = json.dumps({"palabras":palabras})    
    with open("palabrasSilabas.txt", "w") as fileSilabas:
        fileSilabas.write(palabrasJson)
    

