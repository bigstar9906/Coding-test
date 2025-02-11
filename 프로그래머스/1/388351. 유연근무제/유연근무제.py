def timediff(a,b):
#     b-a 로 계산 이후 음수면 더 일찍 출근, 10 이하일 경우 성공(음수 포함)
    a_hour = a//100
    a_min = a%100
    b_hour = b//100
    b_min = b%100
    diff = (b_hour-a_hour)*60+(b_min-a_min)
    return diff<=10
    
    
def solution(schedules, timelogs, startday):
    answer = len(schedules)
    for idx in range(0,len(schedules)):
        today = startday
        for t in timelogs[idx]:
            if (today-1)%7<5 and not timediff(schedules[idx],t):
                answer-=1
                break
            today+=1
                
        
    
        
    return answer