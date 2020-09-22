#!/usr/bin/node
// this class heritance of rectangle

const Rectangle = require('./5-square');

let i, stingc;
class Square extends Rectangle {
  charPrint (c) {
    if (c === undefined) {
      stingc = 'X';
      for (i = 0; i < this.height; i++) {
        console.log(stingc.repeat(this.width));
      }
    } else {
      stingc = c;
      for (i = 0; i < this.height; i++) {
        console.log(stingc.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
