import math
def solution(n):
    num = n-1
    for i in range(2,math.floor(math.sqrt(num))+1):
        if num % i ==0:
            return i
    return num