#!/usr/bin/node

const request = require('request');

// Retrieve the URL from command-line arguments
const url = process.argv[2];

// Make a GET request to the URL
request(url, (error, response) => {
  if (error) {
    console.error('Error:', error);
  } else {
    // Print the status code
    console.log(`code: ${response.statusCode}`);
  }
});
