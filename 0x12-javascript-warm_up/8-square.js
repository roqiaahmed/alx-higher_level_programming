#!/usr/bin/node

const size = process.argv[2];
const item = 'X';

if (!isNaN(size)) {
  for (let i = 0; i < size; i++) {
    console.log(item.repeat(size));
  }
} else {
  console.log('Missing size');
}
