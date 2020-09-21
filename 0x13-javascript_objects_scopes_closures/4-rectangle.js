#!/usr/bin/node
// this is class recngle.

let i;
const myString = 'X';
let tem;
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

  rotate () {
    tem = this.width;
    this.width = this.height;
    this.height = tem;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
