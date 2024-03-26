-- scripts itemize records with same score in second_table table
-- displays score, records count for this score
-- sorted by records in a descending order

SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;