const from = 347312;
const to = 805915;
const mut = [];

const checkAscending = (array) => {
  let lastnum = array[0];
  for (const num of array.slice(1)) {
    if (num < lastnum) {
      return false;
    }
    lastnum = num;
  }
  return true;
};

const checkAdditional = (letters) => {
  let current = letters[0];
  let count = 1;
  const streaks = [];
  letters.slice(1).forEach((letter) => {
    if (letter === current) {
      count++;
    } else {
      streaks.push(count);
      current = letter;
      count = 1;
    }
  });
  streaks.push(count);
  return streaks.includes(2);
};

for (let current = from; current <= to; current++) {
  const str = current.toString();
  const letters = str.split("");
  if (!checkAscending(letters)) continue;
  if (!str.match(/(\d)\1+/)) continue;
  mut.push(letters);
}
console.log(`Part 1: ${mut.length}`);
console.log(`Part 2: ${mut.filter((m) => checkAdditional(m)).length}`);
