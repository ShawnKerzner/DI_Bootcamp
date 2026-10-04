CREATE TABLE items(
item VARCHAR (50) PRIMARY KEY,
price integer
);

CREATE TABLE customers(
	first_name VARCHAR (50) PRIMARY KEY,
	last_name VARCHAR (100)
);

INSERT INTO items(item, price)
VALUES('Small Desk', 100), ('Large Desk', 300), ('Fan', 80);

INSERT INTO customers(first_name, last_name)
VALUES
	('Greg', 'Jones'),
	('Sandra', 'Jones'),
	('Scott', 'Scott'),
	('Trevor', 'Green'),
	('Melanie', 'Johnson');
-- Exercise 1 --
SELECT * FROM items ORDER BY price ASC;

SELECT * FROM items WHERE price >= 80 ORDER BY price DESC;

SELECT last_name FROM customers ORDER BY first_name ASC LIMIT 3;

SELECT last_name FROM customers ORDER BY last_name DESC;

INSERT INTO customers(first_name, last_name) VALUES ('Greg', 'Smith');

