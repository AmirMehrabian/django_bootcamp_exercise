-- Section1
SELECT customers.name, customers.phone FROM customers
JOIN orders ON customers.id = orders.customer_id
GROUP BY customers.id
ORDER BY COUNT(customers.id) DESC
LIMIT 1;

-- Section2
SELECT  foods.id, foods.name
FROM foods 
JOIN  restaurant_foods ON foods.id = restaurant_foods.food_id
JOIN  orders ON restaurant_foods.id = orders.restaurant_food_id 
GROUP BY foods.id 
ORDER BY AVG(orders.rate) DESC, foods.id 
LIMIT  10;

-- Section3
SELECT restaurants.id, restaurants.name 
FROM restaurants
join  restaurant_foods on restaurants.id = restaurant_foods.restaurant_id
join orders on orders.restaurant_food_id = restaurant_foods.id
group by restaurants.id 
order by AVG(orders.rate) desc, restaurants.id asc
LIMIT  10;

-- Section4
SELECT customers.name, customers.phone 
FROM customers
join orders on customers.id = orders.customer_id
join restaurant_foods on restaurant_foods.id = orders.restaurant_food_id
group by customers.id
having COUNT(distinct restaurant_foods.restaurant_id) >= 5
order by customers.name asc;


