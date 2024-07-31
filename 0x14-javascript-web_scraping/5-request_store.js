#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Retrieve the URL and file path from command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the URL
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode === 200) {
    // Write the response body to the file
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.error('Error:', err);
      }
    });
  } else {
    console.error('Error: Failed to retrieve the webpage. Status code:', response.statusCode);
  }
});
