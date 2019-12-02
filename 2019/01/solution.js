const fs = require('fs');
const input = fs.readFileSync('./input.txt', 'utf-8');
const arr = input.split('\n').filter(v => !!v); // remove empty line
const val = arr.reduce((a, v) => a + (Math.floor(parseInt(v) / 3) - 2), 0);
console.log("Part1: ", val);

const val2 = arr.reduce((a, v) => {
	const fuel = (Math.floor(parseInt(v) / 3) - 2);
	let ffuel = fuel;
	let acc = 0;
	while (ffuel > 0) {
		ffuel = (Math.floor(parseInt(ffuel) / 3) - 2);
		acc = ffuel >= 0 ? acc + ffuel : acc;
	}
	return a + acc + fuel;
}, 0);
console.log("Part2: ", val2);