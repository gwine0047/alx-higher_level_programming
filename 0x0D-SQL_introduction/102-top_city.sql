--displays average temperature from top cities
--selction is during the month of July and August.

SELECT CITY, AVG(value) AS avg_temp FROM temperatures WHERE month=7 OR month=8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
