-- 코드를 작성해주세요
SELECT r.ID, IFNULL(g.child_count,0) as child_count
from ECOLI_DATA as r left join (
SELECT p.ID,COUNT(*) as CHILD_COUNT
FROM ECOLI_DATA as p, ECOLI_DATA as c
where p.id = c.parent_id
GROUP BY p.id) as g on r.id = g.id