const fs = require('fs');
const input = fs.readFileSync('./input.txt', 'utf-8').split('\n');
const parseLine = e => {
	const [id, specs] = e.split(' @ ');
	const [coords, dim] = specs.split(': ');
	const [startx, starty] = coords.split(',');
	const [sizex, sizey] = dim.split('x');
	return {
		id,
		startx: parseInt(startx, 10),
		starty: parseInt(starty, 10),
		sizex: parseInt(sizex, 10),
		sizey: parseInt(sizey, 10)
	};
};

const intersection = [];
const compare = (r1, r2) => {};

// #1 @ 493,113: 12x14

for (const line of input) {
	const claim = parseLine(line);
	console.log(claim);
}
