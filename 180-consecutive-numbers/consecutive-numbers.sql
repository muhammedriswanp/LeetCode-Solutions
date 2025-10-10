-- select distinct num as ConsecutiveNums  from (select num, lag(num) over (order by id ) as l, lead(num) over (order by id ) as le
-- from Logs ) as tab
-- where le=num and l=num;

with cte as 
    (select num, 
    lag(num) over (order by id ) as l,
    lead(num) over (order by id ) as le
    from Logs)
     select distinct num as ConsecutiveNums  
     from cte
      where le=num and l=num;
