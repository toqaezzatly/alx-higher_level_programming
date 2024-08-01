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
    const data = JSON.parse(body);
    const films = data.results;
    let count = 0;

    // Iterate over each film to check for the presence of Wedge Antilles (character ID 18)
    for (const film of films) {
      if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        count++;
      }
    }

    // Print the count of movies where Wedge Antilles is present
    console.log(count);
  } else {
    console.log('Error: Unable to retrieve data');
  }
});
