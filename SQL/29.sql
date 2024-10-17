# 더 좋은 풀이가 있을려나...

select t.id, t.student2 as student
from ( 
select s1.id, s1.student2
from ( 
select id, student, ifnull(lead(student, 1) over(order by id), student) as student2
from Seat
) as s1
where mod(s1.id, 2) = 1
union
select s1.id, s1.student2
from ( 
select id, student, ifnull(lag(student, 1) over(order by id), student) as student2
from Seat
) as s1
where mod(s1.id, 2) = 0
) as t
order by t.id