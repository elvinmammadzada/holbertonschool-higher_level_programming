-- Bu script hbtn_0d_usa bazasındakı bütün şəhərləri və onların aid olduğu ştatları siyahıya alır
SELECT cities.id, cities.name, states.name AS state_name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
