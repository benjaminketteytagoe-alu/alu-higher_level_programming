#!/usr/bin/node

const request = require('request');

// Get the movie ID from command line arguments
const movieId = process.argv[2];

// Construct the API URL for the movie
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to get the movie data
request(movieUrl, (error, response, body) => {
  if (error) {
    // Print the error if one occurred
    console.log(error);
  } else {
    // Parse the JSON response
    const movieData = JSON.parse(body);

    // Get the array of character URLs
    const characters = movieData.characters;

    // Fetch and print each character's name
    characters.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
      });
    });
  }
});
