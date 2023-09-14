#!/usr/bin/node

module.exports = class Rectangle {
  constructor(w, h) {
    this.width = w;
    this.height = h;
    if (this.width <= 0 || this.height <= 0 || !this.height || !this.width) {
      this.width = undefined;
      this.height = undefined;
    }
  }
  print() {
    for (let i = 0; i < this.height; i++) {
      console.log("X".repeat(this.width));
    }
  }

  rotate() {
    let temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double() {
    this.width *= 2;
    this.height *= 2;
  }
};
