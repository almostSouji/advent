const fs = require("fs");
const input = fs.readFileSync("./input.txt", "utf-8");
const arr = input.split("\n");
let two = 0;
let three = 0;

for (const element of arr) {
  let hasTwo = false;
  let hasThree = false;
  const symbols = element.split("");
  for (const symbol of symbols) {
    const f = symbols.filter((e) => e === symbol);
    if (f.length === 2) {
      hasTwo = true;
    }
    if (f.length === 3) {
      hasThree = true;
    }
  }
  if (hasTwo) two++;
  if (hasThree) three++;
}

console.log(`Twos: ${two}`);
console.log(`Threes: ${three}`);
console.log(`Checksum: ${two * three}`);
