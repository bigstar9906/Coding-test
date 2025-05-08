from collections import deque
def solution(numbers, target):
    answer = 0
    search = deque()
    search.append([0,0,1])
    search.append([0,0,-1])
    while len(search)>0:
        current = search.popleft()
        value = current[0]+numbers[current[1]]*current[2]
        if current[1]==len(numbers)-1:
            if value==target:
                answer+=1
        else:
            search.append([value,current[1]+1,1])
            search.append([value,current[1]+1,-1])
    return answer