#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId || isNaN(movieId)) {
  console.error('Please provide a valid movie ID as the first argument.');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching data from the Star Wars API:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Unexpected status code:', response.statusCode);
    process.exit(1);
  }

  const filmData = JSON.parse(body);

  // Array to store character URLs
  const characterUrls = filmData.characters;

  // Array to store character names
  const characters = [];

  // Function to fetch character data
  const fetchCharacterData = (characterUrl) => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          reject(`Error fetching character data: ${charError}`);
          return;
        }

        if (charResponse.statusCode !== 200) {
          reject(`Unexpected status code: ${charResponse.statusCode}`);
          return;
        }

        const characterData = JSON.parse(charBody);
        characters.push(characterData.name);
        resolve();
      });
    });
  };

  // Fetch data for each character URL
  Promise.all(characterUrls.map(fetchCharacterData))
    .then(() => {
      console.log('Characters in the movie:');
      characters.forEach((character) => {
        console.log(character);
      });
    })
    .catch((err) => {
      console.error(err);
      process.exit(1);
    });
});
