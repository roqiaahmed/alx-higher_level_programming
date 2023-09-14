#!/usr/bin/node

module.exports = class Square extends Rectangle {
  constructor(size) {
    super(size, size);
  }
  charPrint(c) {
    if (c === "C" || c === "c") {
      for (let i = 0; i < this.size; i++) {
        console.log("C".repeat(this.size));
      }
    } else {
      this.Print();
    }
  }
};
const s1 = new Square(4);
s1.charPrint();

s1.charPrint("C");
