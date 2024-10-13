# select에 냅다 다른 테이블 거 불러와도 됨
select contest_id, round(count(distinct user_id)* 100/ (select count(user_id) from Users), 2) as percentage
from Register
group by contest_id
order by percentage desc, contest_id