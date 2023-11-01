// This script fetches and lists title for all movies using the given url
$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.get(url, function (data) {
    const movies = data.results;
    for (const i in movies) {
      $('#list_movies').append('<li>' + movies[i].title + '</li>');
    }
  });
});
