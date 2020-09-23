#!/usr/bin/node
//  that prints the title of a Star Wars movie where the episode number

const request = require('request');

const urlconsu = process.argv[2];
request(urlconsu, function (error, response, body) {
  let count = 0;
  if (error) {
    console.error('error:', error);
  }
  const resp = JSON.parse(response.body);
  const results = resp.results;
  for (const elem in results) {
    for (const dir in results[elem].characters) {
      if (results[elem].characters[dir] === 'https://swapi-api.hbtn.io/api/people/18/') {
        count += 1;
      }
    }
  }
  console.log(count);
});
