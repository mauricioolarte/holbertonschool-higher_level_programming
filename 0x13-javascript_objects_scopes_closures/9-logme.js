#!/usr/bin/node
//  function that prints the number of arguments already printed and the new

let count = 0;
exports.logMe = function (item) {
    const texttoprint = count + ': ' + item
    console.log(texttoprint)
    count += 1;
}