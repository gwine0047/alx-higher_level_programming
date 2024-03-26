-- scripts lists all records in second_table table
-- omit rows with a name
-- displays both score and name in descending order

SELECT score, name FROM  second_table WHERE name IS NOT NULL AND NAME != '' ORDER BY score DESC;