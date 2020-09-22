#!/usr/bin/node
//  that prints the title of a Star Wars movie where the episode number

const request = require('request');

const urlconsu = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(urlconsu, function (error, response, body) {
    let resp = JSON.parse(response.body)
  console.log(resp['title']); // Print the HTML for the Google homepage.
});
