select p.product_id  , p.product_name 
from Product as p 

where product_id in (select product_id from sales where  sale_date  between '2019-01-01' and   '2019-03-31') and 
p.product_id   not in (
    select product_id from sales where  sale_date < '2019-01-01' or sale_date > '2019-03-31'
)
;