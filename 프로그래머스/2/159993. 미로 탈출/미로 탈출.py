from collections import Counter,deque
def solution(maps):
    answer = 0
    row = len(maps)
    column = len(maps[0])
    start =[]
    end = []
    lever = []
    startToLever = Counter()
    leverToEnd = Counter()
    for r in range(row):
        for c in range(column):
            if maps[r][c]=="S":
                start = [r,c]
            if maps[r][c]=="L":
                lever = [r,c]
            if maps[r][c]=="E":
                end = [r,c]
    queue = deque()
    if start[0]+1<row and maps[start[0]+1][start[1]]!="X":
        queue.append({'position':[start[0]+1,start[1]],'step':1})
        startToLever[str(start[0]+1)+","+str(start[1])]+=1
    if start[0]-1>-1 and maps[start[0]-1][start[1]]!="X":
        queue.append({'position':[start[0]-1,start[1]],'step':1})
        startToLever[str(start[0]+1)+","+str(start[1])]+=1
    if start[1]+1<column and maps[start[0]][start[1]+1]!="X":
        queue.append({'position':[start[0],start[1]+1],'step':1})
        startToLever[str(start[0]+1)+","+str(start[1])]+=1
    if start[1]-1>-1 and maps[start[0]][start[1]-1]!="X":
        queue.append({'position':[start[0],start[1]-1],'step':1})
        startToLever[str(start[0]+1)+","+str(start[1])]+=1
    while len(queue)>0:
        current = queue.popleft()
        if maps[current['position'][0]][current['position'][1]]=="L":
            answer+=current['step']
            break
        if current['position'][0]+1<row and maps[current['position'][0]+1][current['position'][1]] !="X" and startToLever[str(current['position'][0]+1)+","+str(current['position'][1])]==0:
            queue.append({'position':[current['position'][0]+1,current['position'][1]],'step':current['step']+1})
            startToLever[str(current['position'][0]+1)+","+str(current['position'][1])]+=1
        if current['position'][0]-1>-1 and maps[current['position'][0]-1][current['position'][1]] !="X" and startToLever[str(current['position'][0]-1)+","+str(current['position'][1])]==0:
            queue.append({'position':[current['position'][0]-1,current['position'][1]],'step':current['step']+1})
            startToLever[str(current['position'][0]-1)+","+str(current['position'][1])]+=1
        if current['position'][1]+1<column and maps[current['position'][0]][current['position'][1]+1] !="X" and startToLever[str(current['position'][0])+","+str(current['position'][1]+1)]==0:
            queue.append({'position':[current['position'][0],current['position'][1]+1],'step':current['step']+1})
            startToLever[str(current['position'][0])+","+str(current['position'][1]+1)]+=1
        if current['position'][1]-1>-1 and maps[current['position'][0]][current['position'][1]-1] !="X" and startToLever[str(current['position'][0])+","+str(current['position'][1]-1)]==0:
            queue.append({'position':[current['position'][0],current['position'][1]-1],'step':current['step']+1})
            startToLever[str(current['position'][0])+","+str(current['position'][1]-1)]+=1
    if answer==0:
        return -1
    prev = answer
    queue = deque()
    if lever[0]+1<row and maps[lever[0]+1][lever[1]]!="X":
        queue.append({'position':[lever[0]+1,lever[1]],'step':1})
        leverToEnd[str(lever[0]+1)+","+str(lever[1])]+=1
    if lever[0]-1>-1 and maps[lever[0]-1][lever[1]]!="X":
        queue.append({'position':[lever[0]-1,lever[1]],'step':1})
        leverToEnd[str(lever[0]-1)+","+str(lever[1])]+=1
    if lever[1]+1<column and maps[lever[0]][lever[1]+1]!="X":
        queue.append({'position':[lever[0],lever[1]+1],'step':1})
        leverToEnd[str(lever[0])+","+str(lever[1]+1)]+=1
    if lever[1]-1>-1 and maps[lever[0]][lever[1]-1]!="X":
        queue.append({'position':[lever[0],lever[1]-1],'step':1})
        leverToEnd[str(lever[0])+","+str(lever[1]-1)]+=1
    while len(queue)>0:
        current = queue.popleft()
        if maps[current['position'][0]][current['position'][1]]=="E":
            answer+=current['step']
            break
        if current['position'][0]+1<row and maps[current['position'][0]+1][current['position'][1]] !="X" and leverToEnd[str(current['position'][0]+1)+","+str(current['position'][1])]==0:
            queue.append({'position':[current['position'][0]+1,current['position'][1]],'step':current['step']+1})
            leverToEnd[str(current['position'][0]+1)+","+str(current['position'][1])]+=1
        if current['position'][0]-1>-1 and maps[current['position'][0]-1][current['position'][1]] !="X" and leverToEnd[str(current['position'][0]-1)+","+str(current['position'][1])]==0:
            queue.append({'position':[current['position'][0]-1,current['position'][1]],'step':current['step']+1})
            leverToEnd[str(current['position'][0]-1)+","+str(current['position'][1])]+=1
        if current['position'][1]+1<column and maps[current['position'][0]][current['position'][1]+1] !="X" and leverToEnd[str(current['position'][0])+","+str(current['position'][1]+1)]==0:
            queue.append({'position':[current['position'][0],current['position'][1]+1],'step':current['step']+1})
            leverToEnd[str(current['position'][0])+","+str(current['position'][1]+1)]+=1
        if current['position'][1]-1>-1 and maps[current['position'][0]][current['position'][1]-1] !="X" and leverToEnd[str(current['position'][0])+","+str(current['position'][1]-1)]==0:
            queue.append({'position':[current['position'][0],current['position'][1]-1],'step':current['step']+1})
            leverToEnd[str(current['position'][0])+","+str(current['position'][1]-1)]+=1   
    if answer==prev:
        return -1
    return answer