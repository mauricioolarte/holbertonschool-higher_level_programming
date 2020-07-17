-- this is joinig tables
-- generes  From number_of_show=(

SELECT name, count(genre_id) as number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_show_genres.genre_id=tv_genres.id
INNER JOIN tv_shows ON tv_shows.id=tv_show_genres.genre_id
GROUP BY name
ORDER BY number_of_shows DESC;
