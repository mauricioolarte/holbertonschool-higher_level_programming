-- this is a subquery
-- find the cities of california.
SELECT id, name FROM cities
WHERE state_id IN (SELECT id FROM states WHERE name = 'California');
