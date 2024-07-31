from collections import Counter
def solution(book_time):
    answer = 0
    cnt = Counter()
    while len(book_time)>0:
        current = book_time.pop()
        currentStartSplit = current[0].split(":")
        currentEndSplit = current[1].split(":")
        currentStart = int(currentStartSplit[0])*60+int(currentStartSplit[1])
        currentEnd = int(currentEndSplit[0])*60+int(currentEndSplit[1])+10
        for i in range(currentStart,currentEnd):
            cnt[i]+=1
            if cnt[i]>answer:
                answer=cnt[i]        
    return answer