-- 코드를 작성해주세요
SELECT D.ID,D.EMAIL,D.FIRST_NAME,D.LAST_NAME
FROM DEVELOPERS AS D JOIN (SELECT CODE
FROM SKILLCODES
WHERE CATEGORY = 'Front End') AS S ON 1=1
WHERE (D.SKILL_CODE DIV S.CODE)MOD 2 = 1
GROUP BY D.ID,D.EMAIL,D.FIRST_NAME,D.LAST_NAME
ORDER BY ID