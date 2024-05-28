import math
import sys

n = 1000000 # 2부터 1000까지의 모든 수에 대하여 소수 판별
array = [1]*(1000000 + 1) # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제와)
primes = []
# 에라토스테네스의 체 알고리즘
for i in range(3, int(math.sqrt(n)) + 1,2): # 2부터 n의 제곱근까지의 모든 수를 확인하며
    if array[i]: # i가 소수인 경우(남은 수인 경우)
        primes.append(i)
        # i를 제외한 i의 모든 배수를 지우기
        j = i*i
        while j <= n:
            array[j] = 0
            j += i  

while True:
    num = int(sys.stdin.readline())
    if num==0:
        exit()
    idx = 0
    isPrinted = False
    for i in primes:
        if array[num-i]:
            print(str(num)+" = "+str(i)+" + "+str(num-i))
            isPrinted = True
            break
        