#1045
#다시풀기

select customer_id
from Customer
group by customer_id
having count(distinct product_key) = (select count(product_key) from Product)