(select u.name as results      
from Users as u
left join MovieRating as m
on u.user_id = m.user_id
group by u.name
order by count(*) desc,u.name
limit 1)
union all
(select m.title as results      
from Movies as m
left join MovieRating as mr
on m.movie_id    = mr.movie_id  
where  mr.created_at   between  '2020-02-01' and  '2020-02-29'  
group by m.title
order by avg(mr.rating) desc,m.title
limit 1) ;