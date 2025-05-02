from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    onBridge = 0
    onBridge_arr=deque()
    for truck in truck_weights:
        if onBridge+truck>weight:
            while onBridge+truck>weight:
                out = onBridge_arr.pop()
                onBridge-=out[0]
                answer = out[1]+bridge_length
            onBridge_arr.appendleft([truck,answer])
            onBridge+=truck
            if onBridge_arr[-1][1]+bridge_length==answer+1:
                onBridge-=onBridge_arr.pop()[0]
        else:
            answer+=1
            onBridge+=truck
            onBridge_arr.appendleft([truck,answer])
            if onBridge_arr[-1][1]+bridge_length==answer+1:
                onBridge-=onBridge_arr.pop()[0]
    return answer+bridge_length