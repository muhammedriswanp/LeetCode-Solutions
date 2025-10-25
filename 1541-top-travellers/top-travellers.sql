with cte as (
    select user_id  ,sum(distance) as travelled_distance 
    from Rides 
    group by user_id
   
)
select  name     ,coalesce( travelled_distance,0) as travelled_distance
from users as u 
left join cte as c
on c.user_id = u.id
order by travelled_distance desc,name ;


