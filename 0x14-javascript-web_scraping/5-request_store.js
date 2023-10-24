#!/usr/bin/node

const fs = require('fs');
const url = process.argv[2];
const filepath = process.argv[3];
const request = require('request');

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filepath, body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
