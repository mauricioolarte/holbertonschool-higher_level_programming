#!/usr/bin/node
// this is class recngle.

class Rectangle {
  constructor (width, height) {
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }
}

module.exports = Rectangle;
