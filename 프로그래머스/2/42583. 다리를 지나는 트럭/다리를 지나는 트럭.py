from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    on = deque()
    on_time = deque()
    while len(truck_weights)>0:
        if sum(on)+truck_weights[0]<=weight and len(on)+1<=bridge_length:
            on.append(truck_weights[0])
            on_time.append(answer)
            answer+=1
            del truck_weights[0]
        else :
            out = on.popleft()
            out_time = on_time.popleft()
            answer = max(answer,out_time+bridge_length)
    return on_time[-1]+1+bridge_length