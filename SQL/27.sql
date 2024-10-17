#1204
select person_name
from(
    select turn, person_id, person_name, weight, 
    sum(weight) over (order by turn) as total_weight
    from Queue
) as q
where total_weight <= 1000
order by turn desc #마지막으로 타는 인간 추출 
limit 1