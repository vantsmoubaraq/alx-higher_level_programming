-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 13-count_shows_by_genre.sql)
SELECT tv_genres.name
FROM tv_show_genres
        JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
        JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_shows.title = "Dexter"
ORDER BY tv_genres.name ASC;
