from collections import Counter
def solution(n, lost, reserve):
    cnt = Counter()
    rcnt = Counter()
    for r in reserve:
        rcnt[r]+=1
    for l in lost:
        if l in rcnt:
            del(rcnt[l])
        else:
            cnt[l]+=1
    for r in sorted(rcnt):
        if r-1 in cnt:
            del(cnt[r-1])
        elif r+1 in cnt:
            del(cnt[r+1])
    return n-len(cnt)