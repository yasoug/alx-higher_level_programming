// This script fetches the character name from the given url
$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  $.get(url, function (data) {
    $('#character').text(data.name);
  });
});
