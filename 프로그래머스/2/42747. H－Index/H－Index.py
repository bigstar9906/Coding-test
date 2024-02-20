def solution(citations):
    citations.sort(reverse = True)
    answer = 0
    for i in range (0,len(citations)):
        times = len(citations)-i
        for j in range(times):
            if citations[j]<times:
                break
            if j==times-1:
                return times
            
        
        
    return answer