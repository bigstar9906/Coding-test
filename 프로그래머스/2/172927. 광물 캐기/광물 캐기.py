from collections import deque

def solution(picks, minerals):
    # [다이아, 철, 돌]
    iron = {"diamond":5,"iron":1,"stone":1}
    stone = {"diamond":25,"iron":5,"stone":1}
    cnt = 0
    answer = 0
    temp = []
    picks = deque(picks)
    tt = []
    minerals = minerals[:sum(picks)*5]
    for i, p in enumerate(picks):
        if p != 0:
            tt.append((i, p))
    # if len(tt) == 1:
    #     #다이아
    #     if tt[0][0] == 0:
    #         return min(tt[0][1]*5,len(minerals))
    #     elif tt[0][0] == 1:
    #         for m in minerals:
    #             for _ in range(tt[0][1]*5):
    #                 answer += iron[m]
    #         return answer
    #     elif tt[0][0] == 2:
    #         for m in minerals:
    #             for _ in range(tt[0][1]*5):
    #                 answer += stone[m]
    #         return answer
            
    for i in range(0,len(minerals),5):
        a = minerals[i:i+5]
        b = sum([stone[k] for k in a])
        temp.append((minerals[i:i+5], b))
    temp = sorted(temp, key=lambda x: (x[1], len(x[0])))
    print(temp)
    cnt = 0
    while temp:
        if picks:
            a = picks.popleft()
        else:
            break
        for _ in range(a):
            if temp:
                b = temp.pop()[0]
                if cnt == 0:
                    answer += len(b)
                elif cnt == 1:
                    answer += sum([iron[h] for h in b])
                elif cnt == 2:
                    answer += sum([stone[h] for h in b])
            else:
                break
        cnt += 1
    return answer