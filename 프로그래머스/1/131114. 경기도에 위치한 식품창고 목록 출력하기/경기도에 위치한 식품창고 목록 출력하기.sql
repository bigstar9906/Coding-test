-- 코드를 입력하세요
SELECT WAREHOUSE_ID,WAREHOUSE_NAME,ADDRESS,IF(FREEZER_YN is NULL,'N',FREEZER_YN) AS FREEZER_YN
FROM FOOD_WAREHOUSE
WHERE SUBSTRING(ADDRESS,1,2) = '경기'
ORDER BY WAREHOUSE_ID