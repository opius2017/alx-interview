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

  // Use URL list to character pages to make new requests
  for (const charURL of charURLList) {
    await new Promise((resolve, reject) => {
      request(charURL, (err, res, body) => {
        if (err) return console.error(err);

        // Find each character name
        request(JSON.parse(body).name, (err, res, body) => {
          if (err) return console.error(err);

          // Print the character name
          console.log(body);
          resolve();
        });
      });
    });
  }
});
