#!/usr/bin/node

const request = require("request");
const character_ID = 18;
request(process.argv[2], (_err, body) => {
  const res = JSON.parse(body);
  let num;
  for (result in res["results"]) {
    for (character in result["characters"]) {
      let count = character.split(String(character_ID)).length - 1;
      if ((count = 1)) {
        num += 1;
      }
    }
  }
  return num;
});
