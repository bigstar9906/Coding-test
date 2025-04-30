from collections import Counter
def solution(participant, completion):
    answer = ''
    cnt = Counter()
    for p in participant :
        cnt[p]+=1
    for c in completion:
        cnt[c]-=1
    return cnt.most_common()[0][0]