const fs = require("fs");
const input = fs.readFileSync("./input.txt", "utf-8");
const inputArray = input.split(",").filter((v) => !!v);
// promisifying input reading
const { promisify } = require("util");
const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

readline.question[promisify.custom] = (question) => {
  return new Promise((resolve) => {
    readline.question(question, resolve);
  });
};
//

/**
 * Instructions consist of OP-CODES and parameter modes as well as parameters
 * Legal parameters depend on instruction given
 * ABCDE
 * 321OP
 * A,B,C give modes for param 3,2,1
 *
 * MODES:
 * 0 POSITION (use value as position)
 * 1 IMMEDIATE (use value as direct value)
 *
 * OP-CODES:
 * 1 ADD (add p1 + p2, save in p3)
 * 2 MULTIPLY (multiply p1 * p2, save in p3)
 * 3 GET-INPUT (get input, save in p1)
 * 4 PRINT (print p1)
 * 5 JUMP-IF-TRUE (if p1 is non-zero set pointer to p2)
 * 6 JUMP-IF-FALSE (if p1 is zero set pointer to p2)
 * 7 LESS THAN (if p1 is less than p2 store 1 in p3, else store 0 in p3)
 * 9 EQUALS (if p1 equals p2 store 1 in p3, else store 0 in p3)
 * 99 END
 * @param {str[]} Array Array of strings representing integers to use as instructions
 */
const compute = async (arr) => {
  const inArray = arr.slice();
  let pointer = 0;
  let finished = false;
  let maxParamCount = 3;
  while (!finished) {
    const instruction = inArray[pointer];
    const op = parseInt(instruction.toString().slice(-2));
    const modes = instruction
      .toString()
      .slice(0, -2)
      .padStart(maxParamCount, "0");
    // 3 parameter instructions
    if ([1, 2, 7, 8].includes(op)) {
      const p1 =
        modes[2] == 0
          ? parseInt(inArray[inArray[pointer + 1]])
          : parseInt(inArray[pointer + 1]);
      const p2 =
        modes[1] == 0
          ? parseInt(inArray[inArray[pointer + 2]])
          : parseInt(inArray[pointer + 2]);
      if (op === 1) {
        inArray[inArray[pointer + 3]] = p1 + p2;
      } else if (op === 2) {
        inArray[inArray[pointer + 3]] = p1 * p2;
      } else if (op === 7) {
        inArray[inArray[pointer + 3]] = p1 < p2 ? 1 : 0;
      } else {
        inArray[inArray[pointer + 3]] = p1 == p2 ? 1 : 0;
      }
      pointer = pointer + 4;
    }
    // 2 parameter instructions
    else if ([5, 6].includes(op)) {
      const p1 =
        modes[2] == 0
          ? parseInt(inArray[inArray[pointer + 1]])
          : parseInt(inArray[pointer + 1]);
      const p2 =
        modes[1] == 0
          ? parseInt(inArray[inArray[pointer + 2]])
          : parseInt(inArray[pointer + 2]);
      if (op === 5) {
        if (p1) {
          pointer = p2;
        } else {
          pointer = pointer + 3;
        }
      } else {
        if (!p1) {
          pointer = p2;
        } else {
          pointer = pointer + 3;
        }
      }
    }
    // 1 parameter instructions
    else if ([3, 4].includes(op)) {
      if (op === 3) {
        const input = await promisify(readline.question)("Input:\n> ");
        inArray[inArray[pointer + 1]] = parseInt(input);
        readline.close();
      } else {
        const p1 =
          modes[2] == 0 ? inArray[inArray[pointer + 1]] : inArray[pointer + 1];
        console.log(parseInt(p1));
      }
      pointer = pointer + 2;
    }
    // 0 parameter instructions
    else if (op === 99) {
      finished = true;
    }
    // Error
    else {
      console.error(`Unknown OP: ${op}`);
      finished = true;
    }
  }
};

compute(inputArray);
