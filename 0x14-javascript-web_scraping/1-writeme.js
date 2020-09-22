#!/usr/bin/node
// this read a file and print the data

const pathfile = process.argv[2];
const fs = require('fs');
fs.writeFile(pathfile, process.argv[3], function (err, data) {
  if (err) {
    return console.log(err);
  }
//   console.log(data);
});
