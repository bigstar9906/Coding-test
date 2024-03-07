import math
def solution(progresses, speeds):
    answer = []
    prior = 0
    task = 0
    for idx in range(len(progresses)):
        current = math.ceil((100-progresses[idx])/speeds[idx])
        if prior ==0:
            prior = current
            task = 1
        elif current>prior:
            answer.append(task)
            task = 1
            prior = current
        else :
            task+=1
    answer.append(task)
        
    return answer