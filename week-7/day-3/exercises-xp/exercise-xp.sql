SELECT title, description, language.name
FROM film
JOIN language ON film.language_id = language.language_id

SELECT film.title, film.description, name
FROM language
LEFT JOIN film ON language.language_id = film.language_id;

CREATE TABLE new_film (
	id SERIAL PRIMARY KEY,
	name VARCHAR(30)
);

INSERT INTO new_film (name)
VALUES
	('Batman Begins'),
	('The Dark Knight'),
	('The Dark Knight Returns');

SELECT * FROM new_film;

CREATE TABLE customer_review (
	review_id SERIAL PRIMARY KEY,
	film_id INTEGER REFERENCES new_film(id) ON DELETE CASCADE,
	language_id INTEGER REFERENCES language(language_id),
	title VARCHAR(50),
	score INTEGER CHECK(score >=1 AND score <=10),
	review_text TEXT,
	last_update DATE
);

INSERT INTO customer_review(film_id, language_id, title, score, review_text, last_update)
VALUES
	((SELECT id FROM new_film WHERE name = 'Batman Begins'), (SELECT language_id FROM language WHERE name = 'English'), 'Batman Begins Review', 9, 'awesome sauce', '2026-10-05'),
		((SELECT id FROM new_film WHERE name = 'The Dark Knight'), (SELECT language_id FROM language WHERE name = 'English'), 'The Dark Knight Review', 9, 'awesome sauce 2.0', '2026-10-05');

DELETE FROM new_film WHERE name = 'Batman Begins';

SELECT * FROM customer_review;


SELECT * FROM film;


UPDATE film SET language_id = 2 WHERE title = 'Chamber Italian';
UPDATE film SET language_id = 2 WHERE title = 'Grosse Wonderful';
UPDATE film SET language_id = 2 WHERE title = 'Airport Pollack';

-- the fkey is customer_address_id_fkey and it has to exist first in public.address (address_id) where its being referenced or it wont be acepted

DROP TABLE customer_review;
-- Easy step because no other tables are pointing at it for references

SELECT count(*) FROM rental WHERE return_date IS NULL;

SELECT DISTINCT film.title, film.replacement_cost
FROM rental
JOIN inventory ON rental.inventory_id = inventory.inventory_id
JOIN film ON inventory.film_id = film.film_id
WHERE return_date IS NULL
ORDER BY film.replacement_cost DESC
LIMIT 30;

SELECT title
FROM film_actor
JOIN actor on film_actor.actor_id = actor.actor_id
JOIN film on film_actor.film_id = film.film_id
WHERE film.description LIKE '%Sumo%' AND actor.first_name = 'Penelope' and actor.last_name = 'Monroe';

SELECT title
FROM film_category
JOIN film on film_category.film_id = film.film_id
JOIN category on film_category.category_id = category.category_id
WHERE category.name = 'Documentary' AND film.rating = 'R' AND film.length < 60;

SELECT film.title
FROM customer
JOIN rental ON rental.customer_id = customer.customer_id
JOIN payment ON payment.rental_id = rental.rental_id
JOIN inventory ON inventory.inventory_id = rental.inventory_id
JOIN film ON film.film_id = inventory.film_id
WHERE customer.first_name = 'Matthew'
  AND customer.last_name = 'Mahan'
  AND payment.amount > 4.00
  AND rental.return_date >= '2005-07-28'
  AND rental.return_date < '2005-08-02';

SELECT DISTINCT film.title, film.replacement_cost
FROM customer
JOIN rental ON rental.customer_id = customer.customer_id
JOIN inventory ON inventory.inventory_id = rental.inventory_id
JOIN film ON film.film_id = inventory.film_id
WHERE customer.first_name = 'Matthew'
  AND customer.last_name = 'Mahan'
  AND (film.title ILIKE '%boat%' OR film.description ILIKE '%boat%')
ORDER BY film.replacement_cost DESC
LIMIT 1;
