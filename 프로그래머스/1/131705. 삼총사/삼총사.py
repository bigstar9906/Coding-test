from itertools import combinations
def solution(number):
    answer = 0
    idx_list = list(range(len(number)))
    for i in combinations(idx_list,2):
        find = -1*(number[i[0]]+number[i[1]])
        for n in range(len(number)):
            if n not in i and number[n]==find:
                answer+=1
    return answer//3
            