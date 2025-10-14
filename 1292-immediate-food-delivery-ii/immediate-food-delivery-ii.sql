with cte as
(
    select delivery_id ,customer_id ,order_date , rank() over (partition by customer_id order by order_date   ) as ranked ,customer_pref_delivery_date 
    from Delivery 
)
select round((avg(case when order_date = customer_pref_delivery_date then 1 else 0 end ) * 100),2) as immediate_percentage   from cte where ranked =1 ;