from dataclasses import dataclass
import json
from syltippy import syllabize


with open("palabrasJson.txt", "r") as Myfile:
    data = json.load(Myfile)
    
    palabras = []
    
    
    for palabra in data:
        syllabes, stress = syllabize(palabra)
        if(len(syllabes) > 1):
            p = {}
            p["silabas"] = syllabes
            p["palabra"] = palabra
            palabras.append(p)

    palabrasJson = json.dumps({"palabras":palabras})    
    with open("palabrasSilabas.json", "w") as fileSilabas:
        fileSilabas.write(palabrasJson)
    

