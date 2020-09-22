#!/usr/bin/node
// function that returns the reversed version of a list

let i;
exports.esrever = function (list) {
  const newList = [];
  for (i = list.length - 1; i >= 0; i--) {
    newList.splice(0, 0, list[i]);
  }
  return (newList);
};
