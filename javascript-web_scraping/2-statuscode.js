#!/usr/bin/node

const request = require('request');

// Get the URL from command line arguments
const url = process.argv[2];

// Make a GET request to the URL
request(url, (error, response) => {
  if (error) {
    // Print the error if one occurred
    console.log(error);
  } else {
    // Print the status code
    console.log(`code: ${response.statusCode}`);
  }
});
