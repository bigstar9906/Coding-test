from collections import deque
def solution(jobs):
    answer = 0
    len_jobs = len(jobs)
    jobs.sort(key = lambda x: (x[0],x[1]))
    jobs = deque(jobs)
    que = deque()
    time = 0
    current = []
    while len(jobs)>0 or len(que)>0:
        if len(que)<1:
            current = jobs.popleft()
            time = current[0]
        else :
            que = deque(sorted(list(que),key=lambda x: x[1]))
            current = que.popleft()
        time +=current[1]
        answer += time-current[0]
        while len(jobs)>0 and jobs[0][0]<=time:
            que.append(jobs.popleft())
    
    return answer//len_jobs
    
        
            
            