-- this conunt and agroup values of columns
-- count scores.
SELECT score,
COUNT(score) as number
FROM second_table
GROUP BY score DESC;
