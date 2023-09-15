#!/usr/bin/node

const items = process.argv;

if (items.length > 2) {
  if (items.length == 3 && items[2] === '1') {
    console.log(0);
  } else {
    let arr = new Array(items.length - 2);

    for (let i = 0; i < items.length - 2; i++) {
      arr[i] = parseInt(items[i + 2]);
    }
    arr.sort((a, b) => b - a);

    console.log(arr[1]);
  }
} else {
  console.log(0);
}
