#!/usr/bin/node
const stringres = parseInt(process.argv[2]);
if (isNaN(stringres) === false) {
    console.log('My number: ', stringres);
} else {
    console.log('Not a number');
}
