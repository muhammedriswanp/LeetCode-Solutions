select max(n) as num
from
(select max(num) as n
from MyNumbers 
group by num

having count(*)=1 ) as numbers;
