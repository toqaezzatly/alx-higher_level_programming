#!/usr/bin/node

const request = require('request');

// Retrieve the API URL from command-line arguments
const apiUrl = process.argv[2];

// Make a GET request to the API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode === 200) {
    // Parse the JSON response body
    const todos = JSON.parse(body);
    const completedTasks = {};

    // Iterate over each task to count completed tasks by user ID
    todos.forEach(todo => {
      if (todo.completed) {
        if (!completedTasks[todo.userId]) {
          completedTasks[todo.userId] = 0;
        }
        completedTasks[todo.userId]++;
      }
    });

    // Print the result
    console.log(completedTasks);
  } else {
    console.error('Error: Unable to retrieve data. Status code:', response.statusCode);
  }
});
