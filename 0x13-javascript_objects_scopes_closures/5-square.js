#!/usr/bin/node
// this class heritance of rectangle

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor(size) {
    super(size, size);
  }
}
module.exports = Square;
