const fs = require('fs');
const input = fs.readFileSync('./input.txt', 'utf-8');
const arr = input.split('\n');
const numArray = arr.map(e => parseInt(e, 10));

console.log(numArray.reduce((a, e) => a + e));
