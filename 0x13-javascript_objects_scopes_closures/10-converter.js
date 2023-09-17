#!/usr/bin/node
exports.converter = function (base) {
  function convert (a) {
    return a.toString(base);
  }
  return convert;
};
