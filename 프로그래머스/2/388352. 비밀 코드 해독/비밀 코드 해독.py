from itertools import combinations

def solution(n, q, ans):
    whole = range(1,n+1)
    answer = set()
    for idx in range(len(q)):
        current = set()
        for cq in combinations(q[idx],ans[idx]):
            for co in combinations(set(whole)-set(q[idx]),5-ans[idx]):
                current.add(tuple(sorted(cq+co)))
        if len(answer):
            answer = answer & current
        else:
            answer = current
    return len(answer)