-- Section1
SELECT customers.name, customers.phone
FROM customers
JOIN orders ON customers.id = orders.customer_id
JOIN restaurant_foods ON orders.restaurant_food_id = restaurant_foods.id
GROUP BY customers.id
ORDER BY COUNT(DISTINCT restaurant_foods.restaurant_id) DESC, customers.id
LIMIT 1;

-- Section2
SELECT foods.id, foods.name
FROM foods
JOIN restaurant_foods ON foods.id = restaurant_foods.food_id
JOIN orders ON restaurant_foods.id = orders.restaurant_food_id
GROUP BY foods.id
ORDER BY AVG(orders.rate) DESC, foods.id
LIMIT 10;

-- Section3
SELECT restaurants.id, restaurants.name
FROM restaurants
JOIN restaurant_foods ON restaurants.id = restaurant_foods.restaurant_id
JOIN orders ON restaurant_foods.id = orders.restaurant_food_id
GROUP BY restaurants.id
ORDER BY AVG(orders.rate) DESC, restaurants.id
LIMIT 10;

-- Section4
SELECT customers.name, customers.phone
FROM customers
JOIN orders ON customers.id = orders.customer_id
JOIN restaurant_foods ON orders.restaurant_food_id = restaurant_foods.id
GROUP BY customers.id
HAVING COUNT(DISTINCT restaurant_foods.restaurant_id) >= 5
ORDER BY customers.name
LIMIT 10;
