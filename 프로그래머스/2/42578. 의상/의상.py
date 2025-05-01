from collections import Counter
def solution(clothes):
    cnt = Counter()
    answer = 1
    for c in clothes:
        cnt[c[1]]+=1
    for case in cnt:
        answer*=(cnt[case]+1)
    return answer-1