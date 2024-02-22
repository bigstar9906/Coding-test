from collections import deque

def time_diff(a,b):
    a_time = a.split(':')
    b_time = b.split(':')
    
    hh = int(a_time[0])-int(b_time[0])
    mm = int(a_time[1])-int(b_time[1])
    if mm<0 :
        hh-=1
        mm+=60
    return hh*60+mm

def time_add(time,add):
    hh_mm = time.split(':')
    mm = int(hh_mm[1])+int(add)
    if mm>60:
        hh_mm[0] = str(int(hh_mm[0])+mm//60)
        mm= mm%60
    return hh_mm[0]+':'+str(mm)
    
    
def solution(plans):
    answer = []
    doing = deque()
    plans.sort(key=lambda x:x[1])
    plans = deque(plans)
    plan = plans.popleft()
    while len(plans)!=0:
        next = plans.popleft()
        diff = time_diff(next[1],plan[1])
        if diff<int(plan[2]):
            plan[2] = str(int(plan[2])-diff)
            doing.append(plan)
            plan = next
        elif diff==int(plan[2]):
            answer.append(plan[0])
            plan = next
        else :
            answer.append(plan[0])
            extra_time = diff-int(plan[2])
            while len(doing)!=0 and extra_time!=0:
                left = doing.pop()
                if int(left[2])>extra_time:
                    left[2] = str(int(left[2])-extra_time)
                    doing.append(left)
                    extra_time = 0
                else:
                    answer.append(left[0])
                    extra_time-=int(left[2])                
            plan = next
    answer.append(plan[0])
    for i in range(len(doing)):
        answer.append(doing[len(doing)-i-1][0])
    return answer
            
                
        
        
    
    
        
