with cte as (
    select o.sales_id 
    from Orders as o
    left join Company as c
    on o.com_id  = c.com_id 
    where c.name ='RED'
)
select s.name  from SalesPerson as s where sales_id not in (select * from cte) ;