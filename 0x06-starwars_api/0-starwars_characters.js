#!/usr/bin/node
const request = require('request');

const movie = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movie}`;

const makeRequest = (characterUrl) => {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const characterObj = JSON.parse(body);
        resolve(characterObj.name);
      }
    });
  });
};

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieObj = JSON.parse(body);
    const characterUrls = movieObj.characters;

    // Recursive function to process characterUrls one by one
    const processCharacter = (index) => {
      if (index >= characterUrls.length) {
        return; // Base case: all characters processed
      }

      makeRequest(characterUrls[index])
        .then((characterName) => {
          console.log(characterName);
          processCharacter(index + 1); // Process next character
        })
        .catch((error) => {
          console.error(error);
          processCharacter(index + 1); // Process next character
        });
    };

    processCharacter(0); // Start processing from the first character
  }
});
