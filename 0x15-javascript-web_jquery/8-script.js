/* script that fetches and lists all movies title by using this URL:
https://swapi-api.hbtn.io/api/films/?format=json
*/

let i;

$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  let film = '';
  for (i = 0; i < data.results.length; i++) {
    $.get(data.results[i], function (data) {
      film = '<li>' + data.title + '</li>';
      $('#list_movies').append(film);
    });
  }
});
