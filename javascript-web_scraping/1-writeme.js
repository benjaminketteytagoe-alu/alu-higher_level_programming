#!/usr/bin/node

const fs = require('fs');

// Get the file path and content from command line arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Write the content to the file with utf-8 encoding
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    // Print the error object if an error occurred
    console.log(err);
  }
});
