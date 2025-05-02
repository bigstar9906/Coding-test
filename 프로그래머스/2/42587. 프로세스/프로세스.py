from collections import Counter,deque
def solution(priorities, location):
    answer = 1
    cnt = Counter()
    dque = deque()
    idx=0
    for p in priorities:
        cnt[p]+=1
        dque.append({"key":p,"location":idx})
        idx+=1
    while True:
        current = dque.popleft()
        if current["key"]<max(cnt.keys()):
            dque.append(current)
        elif current["location"]==location:
            return answer
        else:
            cnt[current["key"]]-=1
            if cnt[current["key"]]==0:
                del cnt[current["key"]]
            answer+=1
    return 0