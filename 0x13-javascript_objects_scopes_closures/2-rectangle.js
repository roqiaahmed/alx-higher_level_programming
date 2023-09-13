#!/usr/bin/node

class Rectangle {
  constructor(_w, _h) {
    this.width = _w;
    this.height = _h;
    if (this.width <= 0 || this.height <= 0 || !this.height || !this.width) {
      this.width = undefined;
      this.height = undefined;
    }
  }
}
