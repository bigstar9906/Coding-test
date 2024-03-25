from collections import deque
def solution(operations):
    answer = deque()
    for op in operations:
        op = op.split(" ")
        if op[0] == 'I':
            answer.append(int(op[1]))
        elif len(answer)>0:
            answer = deque(sorted(list(answer)))
            if op[1] == '-1':
                answer.popleft()
            else :
                answer.pop()
    if len(answer)<1:
        return [0,0]
    elif len(answer)==1:
        return [answer[0],answer[0]]
    else :
        return [max(answer),min(answer)]