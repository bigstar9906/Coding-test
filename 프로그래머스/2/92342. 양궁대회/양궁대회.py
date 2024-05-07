import itertools
import numpy
def solution(n, info):
    answer = dict()
    infos = []
    apeach = 0
    gain =10
    for i in range(10,0,-1):
        temp = [gain,info[10-i]+1]
        if info[10-i]>0:
            temp[0]+=gain
            apeach+=gain
        infos.append(temp)
        gain-=1
    for i in range(1,11):
        for j in itertools.combinations(infos,i):
            sum_j = numpy.array(j).sum(axis=0)
            if sum_j[0]>apeach and sum_j[1]<=n:
                result = [0,0,0,0,0,0,0,0,0,0]
                left = n
                for num in j:
                    if num[1]>1:
                        result[10-num[0]//2] = num[1]
                        left-=num[1]
                    else:
                        result[10-num[0]] = num[1]
                        left -=num[1]
                result.append(left)                    
                if sum_j[0] in answer:
                    answer[int(sum_j[0])].append(result)
                else:
                    answer[int(sum_j[0])] = [result]
    if len(answer)==0:
        return [-1]
    answer = answer[max(list(answer.keys()))]
    answer.sort(key=lambda x:str(x[::-1]),reverse=True)
    return answer[0]