let i;

$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  let film = '';
  for (i = 0; i < 5; i++) {
    $.get(data.films[i], function (data) {
      film = '<li>' + data.title + '</li>';
      $('#list_movies').append(film);
    });
  }
});
