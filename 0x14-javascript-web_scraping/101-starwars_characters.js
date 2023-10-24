#!/usr/bin/node

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
const request = require('request');
const util = require('util');
const prorequest = util.promisify(request);

request(url, async function test (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const movie = JSON.parse(body);
    for (const character of movie.characters) {
      try {
        const result = await prorequest(character, { json: true });
        console.log(result.body.name);
      } catch (err) {
        console.log(err);
      }
    }
  }
});
