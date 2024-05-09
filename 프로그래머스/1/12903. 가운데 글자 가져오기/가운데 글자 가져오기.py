import math
def solution(s):
    if len(s)%2==0:
        return s[math.floor((len(s)+1)/2)-1]+s[math.ceil((len(s)+1)/2)-1]
    else :
        return s[math.floor((len(s)+1)/2)-1]