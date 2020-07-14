-- this display temperatrut
-- ordered by city and average
SELECT city, AVG(Fahrenheit)
FROM temperatures
ORDER BY AVG(Fahrenheit) DESC;
