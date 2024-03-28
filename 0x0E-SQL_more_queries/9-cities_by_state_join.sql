-- this scripts lists all the California cities in the database hbtn_0d_usa.
-- The record display: cities.id, cities.name and states.name
-- sorted in ascending order by cities.id
-- use only SELECT statement

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.state_id=states.id
ORDER BY cites.id;
