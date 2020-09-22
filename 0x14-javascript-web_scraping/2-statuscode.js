#!/usr/bin/node
//  display the status code of a GET request

const request = require('request');

const urlconsu = process.argv[2];
request.get(urlconsu).on('response', function (response) {
  console.log('code:', response.statusCode);
});
