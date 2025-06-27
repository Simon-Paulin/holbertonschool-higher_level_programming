-- List all show contained
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows_genres
JOIN tv_show
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;