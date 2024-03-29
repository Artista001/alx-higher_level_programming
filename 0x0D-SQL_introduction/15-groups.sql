-- lists the number of records with the same score in the table second_table
-- The result should display the score and the number of records for the score with the label number
-- The list should be sorted by the number of records (descending)
-- The database name will be passed as an argument to the mysql command
SELECT score, COUNT('score') as number
FROM second_table
GROUP BY score
ORDER BY score DESC;
