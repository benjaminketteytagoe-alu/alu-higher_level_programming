#!/usr/bin/node

const request = require('request');

// Get the API URL from command line arguments
const apiUrl = process.argv[2];

// Wedge Antilles character ID
const characterId = '18';

// Make a GET request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    // Print the error if one occurred
    console.log(error);
  } else {
    // Parse the JSON response
    const data = JSON.parse(body);
    
    // Count movies where Wedge Antilles appears
    let count = 0;
    
    // Iterate through all films
    data.results.forEach((film) => {
      // Check if character ID 18 is in the characters array
      film.characters.forEach((characterUrl) => {
        if (characterUrl.includes(`/people/${characterId}/`)) {
          count++;
        }
      });
    });
    
    // Print the count
    console.log(count);
  }
});
