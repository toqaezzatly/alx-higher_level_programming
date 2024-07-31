#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) { console.error('Error', error); } else if (response.statusCode === 200) { const data = JSON.parse(body); console.log(data.title); } else { console.log('Error: Unable to retrieve data'); }
});
