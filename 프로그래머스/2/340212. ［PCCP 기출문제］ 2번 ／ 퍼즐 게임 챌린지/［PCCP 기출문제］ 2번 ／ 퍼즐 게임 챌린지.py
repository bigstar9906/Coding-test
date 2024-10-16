def solution(diffs, times, limit):
    decrease = 0
    beforeT = 0
    time = 0
    levToTime = dict()
    for i in range(len(diffs)):
        currentD = diffs[i]
        currentT = times[i]
        if currentD>1:
            current=currentT+beforeT
            decrease+=current
            if currentD in levToTime:
                levToTime[currentD]+=current
            else:
                levToTime[currentD]=current
        time+=currentT*currentD+beforeT*(currentD-1)
        beforeT = currentT
    level=1
    while time>limit:
        level+=1
        time-=decrease
        if level in levToTime:
            decrease-=levToTime[level]
    return level