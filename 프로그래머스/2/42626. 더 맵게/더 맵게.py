import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        food1 = heapq.heappop(scoville)
        if food1>K-1:
            return answer
        elif len(scoville)==0:
            return -1
        else:
            food2 = heapq.heappop(scoville)
            if food2==0:
                return -1
            else:
                heapq.heappush(scoville,food1+food2*2)
                answer+=1
        