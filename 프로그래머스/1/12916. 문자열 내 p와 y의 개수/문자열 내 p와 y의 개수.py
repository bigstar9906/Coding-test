from collections import Counter
def solution(s):
    cnt = Counter(list(s))
    return cnt['p']+cnt['P'] == cnt['y']+cnt['Y']