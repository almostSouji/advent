const fs = require('fs');
const input = fs.readFileSync('./input.txt', 'utf-8');
const [w1, w2] = input.split('\n').reduce((a, v) => {
		a.push(v.split(',').map(v => ({op: v[0], n: parseInt(v.slice(1))})));
		return a
	}, [])

const getCoord = (arr) => {
	const current = [0, 0];
	const coords = [current.slice()];
	for (const e of arr) {
		let i = 1;
		while ( i < e.n) {
			switch(e.op) {
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
			coords.push(current.slice());
			i++;
		}
	}
	return coords;
}
const [c1, c2] = [getCoord(w1), getCoord(w2)];
console.log("Got coodinates");
const intersections = c1.filter(v => c2.some(w => w[0] === v[0] && w[1] === v[1]))
console.log("Got intersections")
console.log(intersections);
const shortest = intersections.map(v => Math.abs(v[0]) + Math.abs(v[1])).sort((a, b) => a - b)[0]

console.log(`Part 1: ${shortest}`);
