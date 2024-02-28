def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    for res in reserve[:]:
        if res in lost:
            lost.remove(res)
            reserve.remove(res)
    for res in reserve:
        if not reserve:
            break
        if res-1 in lost:
            lost.remove(res-1)
            continue
        if res+1 in lost:
            lost.remove(res+1)
    return n-len(lost)
        