-- 코드를 작성해주세요
select *
from ECOLI_DATA as p, ECOLI_DATA as c
where c.parent_id=p.id