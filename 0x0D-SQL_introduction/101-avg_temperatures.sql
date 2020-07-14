-- this display temperatrut
-- ordered by city and average
SELECT city, AVG(value)
FROM temperatures
GROUP BY city;
