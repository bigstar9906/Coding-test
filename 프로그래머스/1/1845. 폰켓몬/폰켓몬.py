from collections import Counter
def solution(nums):
    answer = Counter(nums)
    return len(answer) if len(nums)/2>len(answer) else len(nums)/2