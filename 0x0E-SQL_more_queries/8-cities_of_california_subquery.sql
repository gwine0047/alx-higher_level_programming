-- this scripts lists all the California cities in the database hbtn_0d_usa.
-- results is sorted by cities in ascending order
-- no use of the key word JOIN.

SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = "California") ORDER BY id;