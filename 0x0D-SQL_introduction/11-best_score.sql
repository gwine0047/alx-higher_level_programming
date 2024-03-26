-- from the table second_table of database hbtn_0c_0
-- records should show both score and name;(ordered by score)

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;