#다시 볼 문제 
select p.product_id, ifnull(round(sum(units * price) / sum(units), 2), 0) as average_price
from UnitsSold u right join Prices p on u.product_id = p.product_id
and u.purchase_date between p.start_date and p.end_date
group by p.product_id

'''
위는 모든 Prices 행을 포함하고 아래는 where 절에 포함되지 않는 것은 없어지게 함 
select p.product_id, ifnull(round(sum(units * price) / sum(units), 2), 0) as average_price
from UnitsSold u right join Prices p on u.product_id = p.product_id
where u.purchase_date between p.start_date and p.end_date
group by p.product_id 

'''