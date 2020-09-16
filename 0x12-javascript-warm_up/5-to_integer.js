#!/usr/bin/node
const stringres = parseInt(process.argv[2]);
if (isNaN(stringres) === false) {
  const strin = 'My number: ' + stringres;
  console.log(strin);
} else {
  console.log('Not a number');
}
