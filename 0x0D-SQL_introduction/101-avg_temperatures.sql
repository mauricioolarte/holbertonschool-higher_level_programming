-- this display temperatrut
-- ordered by city and average
SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY AVG(VALUE) DESC;
