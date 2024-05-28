-- Section1
CREATE INDEX idx1 ON orders (created_at, total);
SELECT sum(total)
FROM orders
WHERE created_at BETWEEN '2020-01-01 00:00:00' AND '2020-12-31 23:59:59';
-- Section2
CREATE INDEX idx2 ON orders (user_id, created_at, total);

SELECT SUM(total)
FROM orders
WHERE created_at BETWEEN '2020-01-01 00:00:00' AND '2020-12-31 23:59:59'
AND user_id = 345;

-- Section3
WITH RECURSIVE all_dates AS (
    SELECT CONVERT('2020-01-01', DATE) AS this_date
    UNION ALL
    SELECT DATE_ADD(this_date, INTERVAL 1 DAY)
    FROM all_dates
    WHERE this_date < '2021-12-11'
)
SELECT all_dates.this_date, COALESCE(SUM(orders.total), 0) AS total_of_day
FROM all_dates
LEFT JOIN orders ON all_dates.this_date = DATE(orders.created_at)
GROUP BY all_dates.this_date
ORDER BY all_dates.this_date ASC;
