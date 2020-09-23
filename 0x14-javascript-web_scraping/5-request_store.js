#!/usr/bin/node
//  that prints the title of a Star Wars movie where the episode number

const request = require('request');
let resp = '';
const urlconsu = process.argv[2];

request(urlconsu, function (error, response, body) {
  if (error) {
    console.error('error:', error);
    return;
  }
  resp = (response.body);
  const pathfile = process.argv[3];
  const fs = require('fs');
  fs.writeFile(pathfile, resp, { encoding: 'utf8' }, function (err, data) {
    if (err) {
      return console.log(err);
    }
  //   console.log(data);
  });
//   console.log(resp)
});
