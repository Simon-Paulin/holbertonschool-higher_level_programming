-- List all cities
SELECT cities.id, cities.name, states.name
From cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;