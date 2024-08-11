import math
def solution(dartResult):
    answer = 0
    before=0
    idx=0
    while idx<len(dartResult):
        current=int(dartResult[idx])
        if dartResult[idx+1]=="0":
            current=10
            idx+=1
        bonus = dartResult[idx+1]
        if idx+2<len(dartResult):
            option = dartResult[idx+2]
        else:
            option="&"
        if bonus =="D":
            current = math.pow(current,2)
        if bonus =="T":
            current = math.pow(current,3)
        if option=="#":
            current*=-1
            idx+=1
        if option=="*":
            current*=2
            answer+=current+before
            idx+=1
        else:
            answer+=current
        before=current
        idx+=2        
    return answer

