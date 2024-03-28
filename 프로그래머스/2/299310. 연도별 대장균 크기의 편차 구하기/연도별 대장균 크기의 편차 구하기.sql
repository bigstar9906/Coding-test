-- 코드를 작성해주세요
SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR,(MAX_SIZE - SIZE_OF_COLONY) AS YEAR_DEV, ID
FROM ECOLI_DATA as e, (SELECT  YEAR(DIFFERENTIATION_DATE) as YEAR, MAX(SIZE_OF_COLONY) AS MAX_SIZE
FROM ECOLI_DATA
GROUP BY YEAR(DIFFERENTIATION_DATE)) as m
where YEAR(e.DIFFERENTIATION_DATE) = m.YEAR
order by 1,2