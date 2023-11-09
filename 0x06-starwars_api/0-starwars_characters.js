#!/usr/bin/node

const request = require('request');
const arg = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${arg}`;
// const url = "https://jsonplaceholder.typicode.com/todos/1"

const requestPromise = new Promise((resolve, reject) => {
  request(url, (error, response, body) => {
    if (error) {
      reject(error);
    } else {
      resolve(JSON.parse(body).characters);
    }
  });
});

requestPromise
  .then((characters) => {
    characters.map((characterUrl) =>
      request(characterUrl, (error, response, body) => {
        if (error) console.log(error);
        body = JSON.parse(body);
        console.log(body.name);
      })
    );
  })
  .catch((error) => {
    console.log(error);
  });
