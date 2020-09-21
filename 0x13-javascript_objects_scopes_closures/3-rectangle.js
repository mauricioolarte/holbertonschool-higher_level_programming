#!/usr/bin/node
// this is class recngle.

let i;
const myString = 'X';
class Rectangle {
  constructor (width, height) {
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    for (i = 0; i < this.height; i++) {
      console.log(myString.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
