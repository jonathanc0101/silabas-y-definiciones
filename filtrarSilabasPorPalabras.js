let fs = require("fs");

const { palabras } = require("./palabras.js");
const {silabas} = require("./silabas");
const silabasNuevas = {};

var stream = fs.createWriteStream("silabasNuevas.txt", { flags: "a" });

for (const palabra of palabras) {
    silabasNuevas[palabra] = silabas[palabra];
  }

stream.write(JSON.stringify(silabasNuevas));

stream.end();