def solution(prices):
    answer = []
    d = dict()
    for i in range(len(prices)):
        answer.append(len(prices)-i-1)
        delete = []
        for k in d.keys():
            if k>prices[i]:
                for idx in d[k]:
                    answer[idx]=i-idx
                delete.append(k)
        for di in delete:
            del d[di]
        if prices[i] in d:
            d[prices[i]].append(i)
        else:
            d[prices[i]]=[i]
    return answer