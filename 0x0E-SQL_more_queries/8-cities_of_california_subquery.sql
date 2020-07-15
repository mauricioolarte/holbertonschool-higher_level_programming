-- this is a subquery
-- find the cities of california.
SELECT id, name FROM states
WHERE id IN (SELECT name FROM cities where state_id = '1')
