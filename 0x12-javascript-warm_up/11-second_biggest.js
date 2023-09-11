#!/usr/bin/node
function SecondBiggest (array) {
  if (array.length < 2) {
    return (0);
  } else {
    array.sort(function (a, b) { return a - b; });
    array.pop();
    return (array.pop());
  }
}
const array = process.argv.slice(2);
console.log(SecondBiggest(array));
