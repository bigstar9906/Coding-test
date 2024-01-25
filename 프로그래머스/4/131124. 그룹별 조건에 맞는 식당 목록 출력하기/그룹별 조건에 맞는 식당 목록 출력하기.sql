-- 코드를 입력하세요
SELECT MEMBER_NAME,REVIEW_TEXT, SUBSTRING(REVIEW_DATE,1,10)AS REVIEW_DATE
FROM REST_REVIEW AS R JOIN 
(SELECT MEMBER_ID FROM REST_REVIEW
GROUP BY MEMBER_ID ORDER BY COUNT(REVIEW_ID) desc limit 1) AS MAX_ID ON R.MEMBER_ID = MAX_ID.MEMBER_ID JOIN MEMBER_PROFILE AS F ON R.MEMBER_ID = F.MEMBER_ID
ORDER BY REVIEW_DATE, REVIEW_TEXT