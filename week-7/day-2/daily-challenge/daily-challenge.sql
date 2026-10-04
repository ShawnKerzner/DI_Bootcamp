CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
);

INSERT INTO FirstTab 
VALUES
	(5,'Pawan'),
	(6,'Sharlee'),
	(7,'Krish'),
	(NULL,'Avtaar');

SELECT * FROM FirstTab;

CREATE TABLE SecondTab (
    id integer 
);

INSERT INTO SecondTab 
VALUES
	(5),
	(NULL);


SELECT * FROM SecondTab;

-- Q1 
-- SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL );
-- Every row gets dropped becuase every rows condition is NULL so its a count of 0 with 1 row

-- Q2
-- SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )

-- it returns one row with a count of two because the row with 5 gets dropped and then the row will null gets dropped as well because we cant compare null to an int and we only keep statements that are true

-- Q3
-- SELECT COUNT(*)
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )
-- This one is checking each one against the whole list so all of them are NULL;

-- -- Q4
-- SELECT COUNT(*)
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )
-- inner returns 5 and in the outer there are two that are not 5 and the null will also be dropped
