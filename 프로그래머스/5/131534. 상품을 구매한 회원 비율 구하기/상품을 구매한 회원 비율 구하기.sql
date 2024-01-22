-- 코드를 입력하세요
SELECT RESULT.*, ROUND(PUCHASED_USERS/UF.UFUSERID,1)AS PUCHASED_RATIO
FROM (SELECT SUBSTRING(O.SALES_DATE,1,4)AS YEAR,CAST(SUBSTRING(O.SALES_DATE,6,2) AS UNSIGNED ) AS MONTH,COUNT(DISTINCT O.USER_ID) AS PUCHASED_USERS
FROM ONLINE_SALE AS O JOIN (SELECT UI.USER_ID FROM USER_INFO AS UI WHERE SUBSTRING(JOINED,1,4)=2021) AS UT ON O.USER_ID = UT.USER_ID
GROUP BY SUBSTRING(O.SALES_DATE,1,4),SUBSTRING(O.SALES_DATE,6,2)) AS RESULT JOIN (SELECT COUNT(USER_ID) AS UFUSERID FROM USER_INFO WHERE SUBSTRING(JOINED,1,4)=2021) AS UF ON 1=1
GROUP BY MONTH
ORDER BY YEAR, MONTH