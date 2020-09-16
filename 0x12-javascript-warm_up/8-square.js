#!/usr/bin/node
let i;
const myString = 'X';
const size = parseInt(process.argv[2]);
if (isNaN(size) === true) {
  console.log('Missing size');
} else {
  for (i = 0; i < size; i++) {
    console.log(myString.repeat(process.argv[2]));
  }
}
