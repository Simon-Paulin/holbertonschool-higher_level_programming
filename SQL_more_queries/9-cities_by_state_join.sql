-- List all cities
SELECT cities.id cities.name state.name
From cities
INNER JOIN states ON cities.state_id = state.id
ORDER BY cities.id ASC;