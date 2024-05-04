from collections import deque
def solution(cap, n, deliveries, pickups):
    answer = 0
    d_idx=deque()
    p_idx=deque()
    d_cap = cap
    p_cap = cap
    for i in range(len(deliveries)-1,-1,-1):
        if len(d_idx)==0 and deliveries[i]!=0:
            d_idx.append(i+1)
        while deliveries[i]>0:
            d_cap-=min(deliveries[i],cap)
            deliveries[i]-=cap
            if d_cap<0:
                d_idx.append(i+1)
                d_cap+=cap
    for i in range(len(pickups)-1,-1,-1):
        if len(p_idx)==0 and pickups[i]!=0:
            p_idx.append(i+1)
        while pickups[i]>0:
            p_cap-=min(pickups[i],cap)
            pickups[i]-=cap
            if p_cap<0:
                p_idx.append(i+1)
                p_cap+=cap
    max_len = max(len(d_idx),len(p_idx))
    for i in range(max_len):
        d_dist = 0
        if len(d_idx)>0:
            d_dist = d_idx.popleft()
        p_dist = 0
        if len(p_idx)>0:
            p_dist = p_idx.popleft()
        answer+=2*max(d_dist,p_dist)
    return answer