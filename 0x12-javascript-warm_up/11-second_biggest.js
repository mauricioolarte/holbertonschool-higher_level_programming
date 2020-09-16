#!/usr/bin/node
if (process.argv.length < 4) {
  console.log('0');
} else {
  let numbers = process.argv.splice(2);
  numbers = numbers.sort(function (a, b) { return b - a; });
  console.log(numbers[1]);
}
