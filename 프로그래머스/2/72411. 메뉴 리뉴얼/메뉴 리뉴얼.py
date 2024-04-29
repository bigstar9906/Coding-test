import itertools
from collections import Counter
def solution(orders, course):
    answer=[]
    orders.sort(key=lambda x:len(x), reverse=True)
    longest = len(orders[0])
    for idx in course:
        if idx>longest:
            continue
        cnt = Counter()
        for order in orders:
            for comb in itertools.combinations(order,idx):
                ordered_comb = sorted(list(comb))
                cnt[''.join(ordered_comb)]+=1
        mc = cnt.most_common()
        if mc[0][1]>1:
            answer.append(mc[0][0])
            for i in range(1,len(mc)):
                if mc[i][1] <mc[0][1]:
                    break
                answer.append(mc[i][0])
    return sorted(answer)