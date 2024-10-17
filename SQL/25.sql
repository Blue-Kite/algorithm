#180
select distinct num0 as ConsecutiveNums
from (
    select id, num as num0,
    lead(num, 1) over(order by id) as num1,
    lead(num, 2) over(order by id) as num2
    from logs
)as t
where t.num0 = t.num1 and t.num1 = t.num2