#!/usr/bin/node

const request = require("request");

request(process.argv[2], (err, body) => {
  if (err) {
    console.log();
  }
  const completedTasksByUsers = {};
  body = JSON.parse(body);
  for (let i = 0; i < body.length; i++) {
    const user_id = body[i].userId;
    const completed = body[i].completed;
    if (completed && !completedTasksByUsers[user_id]) {
      completedTasksByUsers[user_id] = 0;
    }
    if (completed) {
      completedTasksByUsers[user_id] += 1;
    }
  }
  console.log(completedTasksByUsers);
});
