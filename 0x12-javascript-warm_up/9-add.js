#!/usr/bin/node

const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

function add(a, b) {
  if (a & b) {
    const result = a + b;
    console.log(result);
  } else {
    console.log(NaN);
  }
}
add(num1, num2);
