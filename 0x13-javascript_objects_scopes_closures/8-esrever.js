#!/usr/bin/node
exports.esrever = function (list) {
  const reverse = [];
  for (let i = list.length; i > 0; i--) {
    reverse[list.length - i] = list[i - 1];
  }
  return reverse;
};
