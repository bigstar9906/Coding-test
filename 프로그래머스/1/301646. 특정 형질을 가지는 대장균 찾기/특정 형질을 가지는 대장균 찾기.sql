-- 코드를 작성해주세요
SELECT COUNT(*) as COUNT
FROM ECOLI_DATA
WHERE not (GENOTYPE div 2)%2 =1 and (GENOTYPE %2 =1 or (GENOTYPE div 4)%2 =1 )
