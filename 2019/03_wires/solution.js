const fs = require("fs");
const input = fs.readFileSync("./input.txt", "utf-8");
const [w1, w2] = input.split("\n").reduce((a, v) => {
  a.push(v.split(",").map((v) => ({ op: v[0], n: parseInt(v.slice(1)) })));
  return a;
}, []);

const getCoord = (arr) => {
  const current = [0, 0, 0];
  const coords = [];
  for (const e of arr) {
    let i = 1;
    while (i <= e.n) {
      switch (e.op) {
        case "R":
          current[0]++;
          break;
        case "L":
          current[0]--;
          break;
        case "U":
          current[1]++;
          break;
        case "D":
          current[1]--;
          break;
        default:
          console.error("Should not happen");
      }
      current[2]++;
      coords.push(current.slice());
      i++;
    }
  }
  return coords;
};
const [c1, c2] = [getCoord(w1), getCoord(w2)];
console.log("> Got coodinates");
let part1 = Infinity;
let part2 = Infinity;
c1.forEach((v) => {
  return c2.some((w) => {
    if (w[0] === v[0] && w[1] === v[1]) {
      console.log(`Intersection at ${v[0]}, ${v[1]}`);
      const dist = v[2] + w[2];
      const man = Math.abs(v[0]) + Math.abs(v[1]);
      if (dist < part2 && dist > 0) {
        part2 = dist;
      }
      if (man < part1 && man > 0) {
        part1 = man;
      }
      return true;
    }
  });
});
console.log("> Got intersections");
console.log(`Part 1: ${part1}`);
console.log(`Part 2: ${part2}`);
