select id, movie, description, rating
from Cinema
where MOD(id, 2) = 1 and description not like '%boring%'
order by rating desc