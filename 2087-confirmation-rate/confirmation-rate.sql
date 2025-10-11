
    select s.user_id ,
    coalesce (round(count(case when action = 'confirmed' then 1 end) ::decimal / 
    nullif (count(action),0),2), 0.00)  as confirmation_rate 
    from  Signups as s
    left join  Confirmations as c
    on c.user_id  = s.user_id 

    group by s.user_id 

 ;