#!/usr/bin/node

let i; let num; const numbers = []; let sortedNumbers;
const args = process.argv;
const numArgs = process.argv.length;

if (numArgs <= 3) {
  console.log(0);
} else {
  for (i = 2; i < numArgs; i++) {
    num = parseInt(args[i]);
    numbers.push(num);
  }
  sortedNumbers = numbers.sort();
  console.log(sortedNumbers[sortedNumbers.length - 2]);
}
