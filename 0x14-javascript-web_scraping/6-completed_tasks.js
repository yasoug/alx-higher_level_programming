#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const tasks = JSON.parse(body);
    const taskscompleted = {};
    for (const task of tasks) {
      if (task.completed) {
        taskscompleted[task.userId] = (taskscompleted[task.userId] || 0) + 1;
      }
    }
    console.log(taskscompleted);
  }
});
