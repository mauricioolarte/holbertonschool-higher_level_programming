-- this is joinig tables
-- generes  From number_of_show=(

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
LEFT OUTER JOIN tv_genres ON tv_genres.id=tv_show_genres.genre_id
ORDER BY title ASC;
-- ORDER BY name ASC;
