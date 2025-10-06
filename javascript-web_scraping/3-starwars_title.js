#!/usr/bin/node

const request = require('request');

// Get the movie ID from command line arguments
const movieId = process.argv[2];

// Construct the API URL
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API
request(url, (error, response, body) => {
  if (error) {
    // Print the error if one occurred
    console.log(error);
  } else {
    // Parse the JSON response and print the movie title
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  }
});
