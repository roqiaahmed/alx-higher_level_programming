#!/usr/bin/node

const num = process.argv[2];
const parseIntnum = parseInt(num);

if (isNaN(parseIntnum)) {
  console.log("Not a number");
} else {
  console.log(`My number: ${parseIntnum}`);
}
