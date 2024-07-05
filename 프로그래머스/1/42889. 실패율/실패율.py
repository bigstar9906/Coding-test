from collections import Counter, deque
def solution(N, stages):
    people = len(stages)
    fail = 0
    answer = []
    stage = Counter(stages)
    for i in range(N):
        if people==fail:
            answer.append([i+1,0])
        else:
            failer = 0
            if i+1 in stage:
                failer=stage[i+1]
            answer.append([i+1,(failer)/(people-fail)])
            fail+=failer
    answer.sort(key=lambda x:x[1] ,reverse=True)
    return list(map(lambda x:x[0],answer))