const fs = require("fs");
const input = fs.readFileSync("./input.txt", "utf-8");
const inputArray = input
  .split(",")
  .filter((v) => !!v)
  .map((v) => parseInt(v));

const compute = (arr, noun, verb) => {
  const inArray = arr.slice();
  inArray[1] = noun;
  inArray[2] = verb;
  let pointer = 0;
  let finished = false;
  while (!finished) {
    const val = inArray[pointer];
    switch (val) {
      case 1:
        inArray[inArray[pointer + 3]] =
          inArray[inArray[pointer + 1]] + inArray[inArray[pointer + 2]];
        pointer = pointer + 4;
        break;
      case 2:
        inArray[inArray[pointer + 3]] =
          inArray[inArray[pointer + 1]] * inArray[inArray[pointer + 2]];
        pointer = pointer + 4;
        break;
      case 99:
        finished = true;
        break;
      default:
        console.error("Something went wrong...");
        finished = true;
        break;
    }
  }
  return inArray[0];
};

console.log("Part1: ", compute(inputArray, 12, 2));

let res;

const search = () => {
  for (let noun = 0; noun <= 99; noun++) {
    for (let verb = 0; verb <= 99; verb++) {
      const res = compute(inputArray, noun, verb);
      if (res == 19690720) {
        return [noun, verb];
      } else {
        continue;
      }
    }
  }
  return [0, 0];
};
const [noun, verb] = search();

console.log("Part2: ", 100 * noun + verb);
