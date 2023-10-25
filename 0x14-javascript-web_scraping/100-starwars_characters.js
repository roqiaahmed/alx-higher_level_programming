#!/usr/bin/node

const request = require("request");
const flm_url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(flm_url, (err, _res, body) => {
  const characters = JSON.parse(body).characters;
  for (let i = 0; i < characters.length; i++) {
    const character_url = characters[i];
    const character = JSON.parse(character_url).name;
    console.log(character);
  }
});
