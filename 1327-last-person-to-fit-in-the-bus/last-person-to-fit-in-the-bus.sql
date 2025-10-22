with 
    cte as
    (
        select * , sum(Weight) over (order by Turn ) as Total_Weight 
        from  Queue 
        order by Turn 
    ) ,
    cte2 as 
    (
        select * 
        from cte
         where Total_Weight <= 1000
         
    )
        
select person_name  from    Queue where     turn  =    (
            select max(turn)
             from cte2 )   ;