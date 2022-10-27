const { RAE } = require("rae-api");
let fs = require("fs");

const { palabras } = require("./palabras.js");

const debug = false;
const rae = new RAE(debug);

async function buscarPalabra(palabra) {
  const search = await rae.searchWord(palabra);
  const first_result = search.getRes()[0];

  const wordId = first_result.getId();
  const result = await rae.fetchWord(wordId);
  const definitions = result.getDefinitions();

  const nombrePalabra = first_result.getHeader();
  const definiciones = [];

  for (const definition of definitions) {
    definiciones.push(definition.getDefinition());
  }

  const obj = { palabra, definiciones };

  return obj;
}

async function buscarPalabras() {
  resultadoTotal = [];

  var stream = fs.createWriteStream("diccionario.txt", { flags: "a" });

  for (const palabra of palabras) {
    stream.write(JSON.stringify(await buscarPalabra(palabra)));
  }

  stream.end();
}


buscarPalabras();
