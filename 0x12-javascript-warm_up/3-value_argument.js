#!/usr/bin/node

const entry = process.argv.length;
const values = process.argv;

if (entry < 3) {
  console.log('No argument');
} else if (entry >= 3) {
  console.log(values[2]);
}
