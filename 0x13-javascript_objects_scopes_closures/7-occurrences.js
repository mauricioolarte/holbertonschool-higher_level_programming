#!/usr/bin/node
// function that returns the number of occurrences in a list.

let i;
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count += 1;
    }
  }
  return (count);
};
