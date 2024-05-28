-- Section1
create index orders_date on orders(created_at);

    
-- Section2
create index date_and_user_id on orders(user_id, created_at);

-- Section3
with recursive all_dates as(
select convert('2020-01-01', date) as this_date
union all
select date_add(this_date , interval 1 day) from all_dates
where this_date<'2021-12-11'
)

select  all_dates.this_date ,   sum(orders.total) as total_of_day
from all_dates
left join orders on all_dates.this_date = date(orders.created_at)
group by all_dates.this_date 
order by all_dates.this_date  asc;