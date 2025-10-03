select r.contest_id, round((count(r.contest_id  )::decimal/ (select count (* )from Users)* 100),2)
as  percentage 
from Register as r
left join Users as u
on u.user_id = r.user_id 
group by r.contest_id
order by percentage desc,r.contest_id ;