with 
-- cte as 
-- (select p.product_name, o.unit ,  o.product_id   
-- from Products as p
-- join Orders as o
-- on p.product_id  = o.product_id ),

cte2 as(select o.product_id,p.product_name, sum(o.unit) as unit 
from  Orders as o 
join Products as p
on o.product_id = p.product_id
where o.order_date   between   '2020-02-01' and '2020-02-29' 
group by o.product_id ,p.product_name  
having sum(o.unit) >= 100)

 select product_name,unit   from cte2 ;