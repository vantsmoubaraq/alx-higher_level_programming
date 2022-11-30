-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 16-shows_by_genre.sql)
SELECT tv_genres.name FROM tv_genres WHERE tv_genres.name NOT IN (SELECT tv_genres.name FROM tv_show_genres INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id AND tv_shows.title='Dexter' INNER JOIN tv_genres ON tv_genres.id=tv_show_genres.genre_id)
ORDER BY tv_genres.name;
