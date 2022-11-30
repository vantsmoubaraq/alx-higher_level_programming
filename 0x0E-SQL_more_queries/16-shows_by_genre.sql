-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 15-comedy_only.sql)
SELECT tv_shows.title AS 'title', tv_genres.name AS 'name'
FROM tv_shows LEFT OUTER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT OUTER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
ORDER BY title, name;        
