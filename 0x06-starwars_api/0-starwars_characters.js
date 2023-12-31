#!/usr/bin/node
const request = require('request');

const movie = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movie}`;

function getRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) reject(error);

      resolve(JSON.parse(body));
    });
  });
}

async function getCharacters () {
  try {
    const body = await getRequest(url);
    const characters = body.characters;
    for (const characterUrl of characters) {
      const character = await getRequest(characterUrl);
      console.log(character.name);
    }
  } catch (error) {
    console.error(error);
  }
}

getCharacters();
