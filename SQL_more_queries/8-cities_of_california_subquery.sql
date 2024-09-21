-- Lists all the cities of California that can be found on the database
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California');