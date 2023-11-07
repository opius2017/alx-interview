#!/usr/bin/node
/**
 * Prints all characters of a Star Wars movie
 * The first positional argument passed is the Movie ID
 * Display one character name per line in the same order
 * as the list in the /films/ endpoint
 */

const request = require('request');
const filmNum = process.argv[2] + '/';
const filmURL = 'https://swapi-api.hbtn.io/api/films/';

// Make an API request to get the film details
request(filmURL + filmNum, async (err, res, body) => {
  if (err) return console.error(err);

  // Find URLs of each character in the film as a list obj
  const charURLList = JSON.parse(body).characters;

  // Function to make requests in order
  const getCharacter = (charURL) => {
    request(charURL, (err, res, body) => {
      if (err) return console.error(err);

      // Find each character name
      const character = JSON.parse(body);
      console.log(character.name);

      // Move to the next character, if available
      const nextCharacterURL = charURLList.shift();
      if (nextCharacterURL) {
        getCharacter(nextCharacterURL);
      }
    });
  };

  // Start the process with the first character
  const firstCharacterURL = charURLList.shift();
  if (firstCharacterURL) {
    getCharacter(firstCharacterURL);
  }
});

