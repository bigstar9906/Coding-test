from collections import deque
def check(place):
    x_d=[0,0,-1,1]
    y_d=[1,-1,0,0]
    for i in range(5):
        for j in range(5):
            if place[i][j]=='P':
                stack = deque()
                for d in range(4):
                    cur_i = i-y_d[d]
                    cur_j = j-x_d[d]
                    if cur_i in range(5) and cur_j in range(5):
                        cur = place[cur_i][cur_j]
                        if cur=='P':
                            return 0
                        if cur=='O':
                            stack.append([cur_i,cur_j])
                for s in stack:
                    for d in range(4):
                        cur_i = s[0]-y_d[d]
                        cur_j = s[1]-x_d[d]
                        if cur_i in range(5) and cur_j in range(5):
                            cur = place[cur_i][cur_j]
                            if cur=='P' and [i,j]!=[cur_i,cur_j]:
                                return 0
    return 1

def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))
    return answer