from collections import Counter
def solution(points, routes):
    answer =0
    cnt = Counter()
    for r in routes:
        time = 0
        isStart = 0
        for i in range(len(r)-1):
            x1 = points[r[i]-1][0]
            x2 = points[r[i+1]-1][0]
            y1 = points[r[i]-1][1]
            y2 = points[r[i+1]-1][1]
            step = 1 if x2>x1 else -1
            for idx in range(x1+(isStart*step),x2+step,step):
                isStart=1
                time+=1
                cnt[str([idx,y1,time])]+=1
            step = 1 if y2>y1 else -1
            for idx in range(y1+(isStart*step),y2+step,step):
                isStart=1
                time+=1
                cnt[str([x2,idx,time])]+=1
    for c in cnt:
        if cnt[c]>1:
            answer+=1
    return answer