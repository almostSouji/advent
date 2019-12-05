const fs = require('fs');
const input = fs.readFileSync('./input.txt', 'utf-8');
const inputArray = input.split(',').filter(v => !!v);
const { promisify } = require('util');
const readline = require('readline').createInterface({
	input: process.stdin,
	output: process.stdout
})

readline.question[promisify.custom] = (question) => {
	return new Promise((resolve) => {
	  readline.question(question, resolve);
	});
};

const compute = async (arr) => {
	const inArray = arr.slice();
	console.log(inArray[6]);
	console.log(inArray[225]);
	let pointer = 0;
	let finished = false;
	let maxParamCount = 3;
	while (!finished) {
		const instruction = inArray[pointer];
		const op = parseInt(instruction.toString().slice(-2));
		const modes = instruction.toString().slice(0, -2).padStart(maxParamCount, "0");
		console.log("----")
		console.log(`Ins: ${instruction}`);
		console.log(`OP: ${op}`);
		console.log(`MOD: ${modes}`);
		console.log(inArray);
		// 321 <-- params the mode is for
		// 000op
		// mode 0 = position
		// mode 1 = immediate
		// 3 parameters
		if ([1,2].includes(op)) {
			// parse
			const p1 = modes[2] == 0 ?  parseInt(inArray[inArray[pointer + 1]]) : parseInt(inArray[pointer + 1]);
			const p2 = modes[1] == 0 ?  parseInt(inArray[inArray[pointer + 2]
			]) : parseInt(inArray[pointer + 2]);
			console.log(`P1: ${p1}`)
			console.log(`P2: ${p2}`)
			console.log(`P3: ${inArray[pointer + 3]}`);
			if (op === 1) {
				inArray[inArray[pointer + 3]] = p1 + p2;
			} else {
				inArray[inArray[pointer + 3]] = p1 * p2;
			}
			pointer = pointer + 4;
		}
		// 1 param
		else if ([3, 4].includes(op)) {
			// parse
			if (op === 3) {
				const input = await promisify(readline.question)('Unit to test:\n> ');
				inArray[inArray[pointer + 1]] = parseInt(input);
				readline.close();
			} else {
				const p1 = modes[2] == 0 ?  inArray[inArray[pointer + 1]] : inArray[pointer + 1];
				console.log(parseInt(p1));
			}
			pointer = pointer + 2
		}
		// no param
		else if (op === 99) {
			finished = true;
		}
		else {
			console.error(`Unknown OP: ${op}`);
			finished = true;
		}
	}
	return inArray[0];
}

compute(inputArray);