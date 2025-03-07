select LEFT(trans_date, 7) as month, country, 
count(id) as trans_count,  count(if(state like 'approved', id, null)) as approved_count,
sum(amount) as trans_total_amount, 
sum(if(state like 'approved', amount, 0)) as approved_total_amount
from Transactions
group by country, month