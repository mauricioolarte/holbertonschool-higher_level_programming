#!/usr/bin/node
// function that converts a number from base 10 to another base passed as argument

const list = require('./100-data').list;

let count = 0;
const newlist = list.map(changelist)
function changelist (ind) {
  value = ind * count;
  count += 1;
  return (value);   
};
console.log(list);
console.log(newlist);
