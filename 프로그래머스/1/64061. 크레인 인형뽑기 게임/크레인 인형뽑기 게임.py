from collections import deque
def solution(board, moves):
    answer = 0
    doll_line = dict()
    bucket = deque()
    for i in range(len(board[0])):
        doll_line[i+1]=deque()
        for j in range(len(board)):
            if board[j][i]!=0:
                doll_line[i+1].appendleft(board[j][i])
    for m in moves:
        if len(doll_line[m])>0:
            current = doll_line[m].pop()
            if len(bucket)>0 and bucket[-1]==current:
                bucket.pop()
                answer+=2
            else:
                bucket.append(current)
    return answer