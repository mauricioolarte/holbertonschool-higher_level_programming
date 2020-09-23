#!/usr/bin/node
//  that prints the title of a Star Wars movie where the episode number

const request = require('request');


const urlconsu = process.argv[2];
request(urlconsu, function (error, response, body) {
  const respuesta = {};
  if (error) {
    console.error('error:', error);
  }
  const resp = JSON.parse(response.body);
  for (const task in resp) {
    if (resp[task].completed === true) {
      if (!(respuesta[resp[task].userId.toString()])) {
        respuesta[resp[task].userId.toString()] = 0;
      }
      respuesta[resp[task].userId.toString()] = parseInt(respuesta[resp[task].userId.toString()]) + 1;
    }
  }
  console.log(respuesta);
});
