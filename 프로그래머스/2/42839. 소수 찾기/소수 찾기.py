from collections import Counter
import itertools
import math
def isPrime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
        
def solution(numbers):
    answer = 0
    nums = Counter()
    for i in range(1,len(numbers)+1):
        for num in itertools.permutations(numbers,i):
            nums[int(''.join(num))]+=1
    for key in nums.keys():
        if isPrime(key):
            print(key)
            answer+=1
            
    return answer