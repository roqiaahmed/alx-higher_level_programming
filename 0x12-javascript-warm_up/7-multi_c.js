#!/usr/bin/node

const arg = process.argv[2];
const C = "C is fun";

if (!isNaN(arg)) {
  for (let i = 0; i < arg; i++) {
    console.log(C);
  }
} else {
  console.log('Missing number of occurrences');
}
