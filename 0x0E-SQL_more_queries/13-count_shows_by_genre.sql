-- this is joinig tables
-- generes  From number_of_show=(

SELECT name, COUNT(genre_id) AS number_of_shows
FROM (SELECT tv_genres.name, tv_show_genres.genre_id
FROM tv_genres
INNER JOIN tv_show_genres ON tv_show_genres.genre_id=tv_genres.id) AS geres
GROUP BY name
ORDER BY number_of_shows DESC;




/*
(SELECT tv_genres.name, tv_show_genres.genre_id
FROM tv_genres
INNER JOIN tv_show_genres ON tv_show_genres.genre_id=tv_genres.id)
*/
