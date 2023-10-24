#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const id = '/people/18/';

request(url, (err, code, body) => {
  if (err) {
    console.log(err);
  } else {
    const count = body.split(id).length - 1;
    console.log(count);
  }
});
