#1070
select s.product_id, s.year as first_year, s.quantity, s.price
from Sales s left join Product p on s.product_id = p.product_id
where (s.product_id, s.year) in (
    select s.product_id, min(s.year)
    from Sales s left join Product p on s.product_id = p.product_id
    group by s.product_id
)