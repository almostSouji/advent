const fs = require("fs");
const input = fs.readFileSync("./input.txt", "utf-8");
const arr = input.split("\n");
const numArray = arr.map((e) => parseInt(e, 10));
let found = false;
const frequencies = new Set();
let it = 0;

while (!found) {
  for (const e of numArray) {
    it += e;
    if (frequencies.has(it)) {
      found = true;
      return console.log(it);
    }
    frequencies.add(it);
  }
}
