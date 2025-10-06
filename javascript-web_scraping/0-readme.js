#!/usr/bin/node

const fs = require('fs');

// Get the file path from command line arguments
const filePath = process.argv[2];

// Read the file with utf-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    // Print the error object if an error occurred
    console.log(err);
  } else {
    // Print the file content
    console.log(data);
  }
});
