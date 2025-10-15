select id , case when mod(id,2)=0 then lag(student ,1) over (order by id ) 
else lead(student,1,student) over (order by id )  end as student 
from Seat ;