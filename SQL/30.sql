# Write your MySQL query statement below
(select u.name as results 
from MovieRating r join Users u on r.user_id = u.user_id
group by u.user_id
order by count(u.user_id) desc, u.name 
limit 1)
union all
(select m.title as results
from MovieRating r join Movies m on r.movie_id = m.movie_id
where year(created_at) = '2020' and month(created_at) = '02'
group by m.movie_id
order by avg(r.rating) desc, m.title
limit 1)