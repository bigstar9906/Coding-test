import math
def solution(n):
    isPrime = list(range(n+1))
    for i in range(2,int(math.sqrt(n)+1)):
        if isPrime[i]==0:
            continue
        for j in range(i*i,n+1,i):
            isPrime[j]=0
    return len([i for i in isPrime[2:] if isPrime[i]])