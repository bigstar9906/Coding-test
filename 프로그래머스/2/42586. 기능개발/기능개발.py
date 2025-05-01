import math
def solution(progresses, speeds):
    answer = []
    temp = [math.ceil((100-progresses[0])/speeds[0]),0]
    for i in range(1,len(progresses)):
        current = math.ceil((100-progresses[i])/speeds[i])
        if temp[0]<current:
            answer.append(i-temp[1])
            temp=[current,i]
    answer.append(len(progresses)-temp[1])
        
    return answer