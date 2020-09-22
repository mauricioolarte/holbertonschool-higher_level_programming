#!/usr/bin/node
// function that converts a number from base 10 to another base passed as argument
let inputbase = 10;
exports.converter = function (base) {
    let inputbase = base;
    the_base_number = base;
    return(inputbase.toString(the_base_number));
}
console.log(this.converter(10))
console.log(this.converter(2))
