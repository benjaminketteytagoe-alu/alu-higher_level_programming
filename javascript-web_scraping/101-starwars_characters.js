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

    // Function to print character names in order
    const printCharacter = (index) => {
      if (index >= characters.length) {
        return; // Base case: all characters printed
      }

      // Fetch the character at the current index
      request(characters[index], (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
        // Recursively print the next character
        printCharacter(index + 1);
      });
    };

    // Start printing from the first character
    printCharacter(0);
  }
});
