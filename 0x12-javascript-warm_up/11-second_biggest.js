#!/usr/bin/node

let i; let num; const numbers = [];
const args = process.argv;
const numArgs = process.argv.length;

if (numArgs <= 3) {
  console.log(0);
} else {
  for (i = 2; i < numArgs; i++) {
    num = parseInt(args[i]);
    if (isNaN(num)) {
      continue;
    } else {
      numbers.push(num);
    }
  }
  console.log(numbers.sort()[numbers.length - 2]);
}
