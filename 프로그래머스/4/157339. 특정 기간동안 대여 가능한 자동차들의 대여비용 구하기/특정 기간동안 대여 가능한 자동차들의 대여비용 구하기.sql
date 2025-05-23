-- 코드를 입력하세요
SELECT F.CAR_ID,F.CAR_TYPE,F.FEE FROM 
(SELECT C.CAR_ID,C.CAR_TYPE,ROUND(C.DAILY_FEE*0.3*(100-P.DISCOUNT_RATE),0) AS FEE
FROM CAR_RENTAL_COMPANY_CAR AS C JOIN  CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS P ON C.CAR_TYPE = P.CAR_TYPE
WHERE (C.CAR_TYPE = 'SUV' or C.CAR_TYPE = '세단') and LEFT(P.DURATION_TYPE,2)='30'and FLOOR(C.DAILY_FEE*0.3*(100-LEFT(P.DISCOUNT_RATE,1))) between 500000 and 1999999) AS F LEFT JOIN (
    SELECT H.CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H
    WHERE H.START_DATE between "2022-11-01" and "2022-11-30"
    or H.END_DATE between "2022-11-01" and "2022-11-30"or "2022-11-01" between H.START_DATE AND H.END_DATE
    ) AS A ON F.CAR_ID = A.CAR_ID
WHERE IFNULL(A.CAR_ID,"")=""
ORDER BY 3 DESC,2,1 DESC