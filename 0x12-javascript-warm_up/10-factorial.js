#!/usr/bin/node

function factorial (a) {
  if (process.argv.lenght < 3 || isNaN(a) === true) {
    return 1;
  }
  if (a >= 1) {
    return a * factorial(a - 1);
  } else if (a === 0) {
    return 1;
  }
}
console.log(factorial(parseInt(process.argv[2])));
