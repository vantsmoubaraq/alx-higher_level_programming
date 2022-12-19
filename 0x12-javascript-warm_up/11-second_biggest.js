#!/usr/bin/node

let i;
const args = process.argv;
const numArgs = process.argv.length;

if (numArgs <= 3) {
  console.log(0);
} else {
  for (i = 2; i < numArgs; i++) {
    parseInt(args[i]);
  }
  console.log(args.sort()[numArgs - 2]);
}
