#!/usr/bin/node
// function that converts a number from base 10 to another base passed as argument

exports.converter = function (base) {
  function changebase (value) {
    return (value.toString(base));
  }
  return changebase;
};
