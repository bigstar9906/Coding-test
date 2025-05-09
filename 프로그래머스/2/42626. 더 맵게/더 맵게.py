import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville)>1:
        min1 = heapq.heappop(scoville)
        if min1>=K:
            return answer
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville,min1+min2*2)
        answer+=1
    return answer if scoville[0]>=K else -1