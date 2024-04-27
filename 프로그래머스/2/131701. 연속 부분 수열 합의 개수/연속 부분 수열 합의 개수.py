from collections import Counter
def solution(elements):
    answer = Counter()
    length = len(elements)
    for i in range(length):
        val = 0
        for j in range(length):
            val += elements[(i+j)%length]
            answer[val]+=1
    return len(answer)
        