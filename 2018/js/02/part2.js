const fs = require("fs");
const input = fs.readFileSync("./input.txt", "utf-8");
const arr = input.split("\n");
const arar = arr.map((e) => e.split(""));

arar.forEach((line, index) => {
  if (index === arar.length - 1) {
    return;
  }
  arar.forEach((l) => {
    const one = line;
    const two = l;
    let diff = 0;
    const comm = [];
    one.forEach((char, ci) => {
      const cOne = char;
      const cTwo = two[ci];

      if (cOne === cTwo) {
        comm.push(cOne);
      } else {
        diff++;
      }
    });
    if (diff === 1) {
      return console.log(comm.join(""));
    }
  });
});
