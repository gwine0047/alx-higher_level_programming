-- script displays the average temperature.
-- it is grouped by city, ordered descendingly by the average temperature.

SELECT `city`, AVG(`value`) AS avg_temp
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` ESC;
