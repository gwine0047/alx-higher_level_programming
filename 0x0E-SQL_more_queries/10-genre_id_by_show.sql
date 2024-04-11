-- This scripts lists all shows contained in the hbtn_0d_tvshows thats have atleast a genre in common.
-- the record should show the following: tv_show_genres.genre_id.id, tv_shows.title
-- sorted in ascending order by tv_shows.title and tv_show_genres. genre_id
-- use  only SELECT statement

SELECT tv.shows.title,tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
