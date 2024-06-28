from itertools import combinations
import math
def isPrime(num):
    if num<2:
        return False
    if num ==2:
        return True
    for i in range(2,math.floor(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True

def solution(nums):
    answer = 0
    for num in list(combinations(nums,3)):
        if isPrime(sum(num)):
            answer+=1
    return answer