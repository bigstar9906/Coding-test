import math
def solution(n):
    answer=0
    for i in range(1,math.floor(math.sqrt(n)+1)):
        if n%i==0:
            answer+=i
            if n//i!=i:
                answer+=n//i
    return answer