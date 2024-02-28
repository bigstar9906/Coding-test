from collections import Counter
def solution(clothes):
    answer = 1
    cloth_count = Counter()
    for cloth in clothes:
        cloth_count[cloth[1]]+=1
    for sortOf in cloth_count.keys():
        answer*=cloth_count[sortOf]+1
    
    return answer-1