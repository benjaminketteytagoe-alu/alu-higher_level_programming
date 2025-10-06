#!/usr/bin/node

const request = require('request');

// Get the API URL from command line arguments
const apiUrl = process.argv[2];

// Make a GET request to the API
request(apiUrl, (error, response, body) => {
  if (error) {
    // Print the error if one occurred
    console.log(error);
  } else {
    // Parse the JSON response
    const todos = JSON.parse(body);

    // Object to store completed tasks count per user
    const completedTasks = {};

    // Iterate through all todos
    todos.forEach((todo) => {
      // Only count completed tasks
      if (todo.completed) {
        // Initialize counter for user if not exists
        if (!completedTasks[todo.userId]) {
          completedTasks[todo.userId] = 0;
        }
        // Increment the count for this user
        completedTasks[todo.userId]++;
      }
    });

    // Print the completed tasks object
    console.log(completedTasks);
  }
});
