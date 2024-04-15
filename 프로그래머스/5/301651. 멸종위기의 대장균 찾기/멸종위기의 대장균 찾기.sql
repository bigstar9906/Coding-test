-- 코드를 작성해주세요
WITH RECURSIVE ECOLI_LVL(ID,PARENT_ID,LVL)
AS(
    SELECT ID, PARENT_ID, 1 AS LVL
    FROM ECOLI_DATA
    WHERE PARENT_ID is NULL
    
    UNION
    
    SELECT a.ID, a.PARENT_ID, b.LVL+1
    FROM ECOLI_DATA a
    JOIN ECOLI_LVL AS b
    ON a.PARENT_ID = b.ID
)
SELECT COUNT(*) AS COUNT,LVL AS GENERATION
FROM ECOLI_LVL NATURAL JOIN (SELECT P.ID FROM ECOLI_DATA AS P LEFT OUTER JOIN ECOLI_DATA AS C ON P.ID=C.PARENT_ID WHERE C.ID is NULL) AS NO_CHILD
GROUP BY LVL
ORDER BY 2