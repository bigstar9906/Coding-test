from collections import Counter
def solution(nums):
    cnt = Counter()
    for n in nums:
        cnt[n]+=1
    return min(len(nums)//2,len(cnt))