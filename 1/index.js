const fs = require('fs');
const input = fs.readFileSync('./input.md', 'utf-8');
const arr = input.split('\n');
const numArray = arr.map(e => parseInt(e, 10));
let found = false;
const frequencies = [];
let it = 0;
while (!found) {
	for (const e of numArray) {
		it += e;
		if (frequencies.includes(it)) {
			found = true;
			return console.log(it);
		}
		frequencies.push(it);
	}
}

