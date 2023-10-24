#!/usr/bin/node

const request = require("request");
const url = "https://swapi-api.alx-tools.com/api/films/".concat(
  process.argv[2]
);
request(url, (body) => {
  film = JSON.parse(_err, _res, body);
  console.log(film.title);
});
