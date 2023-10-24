#!/usr/bin/node

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
const request = require('request');

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const movies = JSON.parse(body);
    for (const character of movies.characters) {
      request(character, (err, response, body) => {
        const names = JSON.parse(body);
        if (err) {
          console.log(err);
        } else {
          console.log(names.name);
        }
      });
    }
  }
});
