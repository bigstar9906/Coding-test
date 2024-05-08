from collections import deque
import math

def isPrime(n):
    if n<2:
        return False
    if n==2:
        return True
    for i in range(2,math.ceil(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def solution(n, k):
    answer = 0
    now = ''
    while n>0:
        t = n%k
        if t==0:
            if now!='':
                if isPrime(int(now)):
                    answer+=1
            now = ''
        else:
            now = str(t)+now
        n = n//k
    if isPrime(int(now)):
        answer+=1
    return answer