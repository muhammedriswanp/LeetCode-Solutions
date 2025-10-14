with cte as(
    select player_id, min(event_date ) as first_login_date
    from Activity
    group by  player_id 
) , cte2 as
 ( 
select * 
from cte as cte 
join Activity as a 
on cte.player_id  = a.player_id and a.event_date = cte.first_login_date + interval '1 day' ) 

select 
round( count(*)::decimal/(select  count(distinct player_id) from Activity  ),2) as fraction 
 from cte2 ;