import json
from syltippy import syllabize


with open("palabrasJson.txt", "r") as Myfile:
    data = json.load(Myfile)
    
    palabras = {}

    for palabra in data:
        syllabes, stress = syllabize(palabra)
        palabras[palabra] = syllabes

        # print(palabra)
        # print(syllabes)

    palabrasJson = json.dumps(palabras)    
    with open("palabrasSilabas.txt", "w") as fileSilabas:
        fileSilabas.write(palabrasJson)
    

