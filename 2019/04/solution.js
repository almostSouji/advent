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
}

for (let current = from; current <= to; current++) {
	const str = current.toString();
	const letters = str.split('');
	if (!checkAscending(letters)) continue;
	if (!str.match(/(\d)\1+/)) continue;
	console.log(`Adding ${current} to valid mutations`)
	mut.push(current);	
}
console.log(`Part 1: ${mut.length}`);