#!/usr/bin/node

module.exports = class Square extends require("./5-square.js") {
  constructor(size) {
    super(size, size);
  }
  charPrint(c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log("C".repeat(this.height));
      }
    }
  }
};
