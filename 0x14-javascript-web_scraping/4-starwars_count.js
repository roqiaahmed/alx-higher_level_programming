#!/usr/bin/node

const request = require("request");
const character_ID = 18;
let times = 0;
request(process.argv[2], (_err, _res, body) => {
  body = JSON.parse(body).results;
  for (let i = 0; i < body.length; i++) {
    const characters = body[i].characters;
    for (let j = 0; j < characters.length; j++) {
      const character = characters[j];
      if (character.split("/")[5] === String(character_ID)) {
        times += 1;
      }
    }
  }
  console.log(times);
});
