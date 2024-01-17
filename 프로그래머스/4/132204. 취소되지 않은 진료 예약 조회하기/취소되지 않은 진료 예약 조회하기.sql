-- 코드를 입력하세요
SELECT a.APNT_NO, p.PT_NAME, p.PT_NO, a.MCDP_CD, d.DR_NAME,a.APNT_YMD
from appointment as a left join patient as p on a.PT_NO = p.PT_NO left join doctor as d on a.MDDR_ID = d.DR_ID
where a.APNT_CNCL_YN = 'N' and SUBSTR(a.APNT_YMD,1,10)='2022-04-13'
order by a.APNT_YMD