from collections import deque
def solution(board):
    start_index = []
    visited = dict()
    queue = deque()
    for row in board:
        if 'R'in row:
            start_index = [board.index(row),row.index('R')]
            visited[str(start_index)]=1
    UDLR_x = [0,0,-1,1]
    UDLR_y = [-1,1,0,0]
    for i in range(4):
        next_index = [start_index[0]+UDLR_y[i],start_index[1]+UDLR_x[i]]
        while next_index[0]<len(board) and next_index[0]>-1 and next_index[1]<len(board[0]) and next_index[1]>-1 and board[next_index[0]][next_index[1]]!='D':
            next_index = [next_index[0]+UDLR_y[i],next_index[1]+UDLR_x[i]]
        current_index = [next_index[0]-UDLR_y[i],next_index[1]-UDLR_x[i]]
        if board[current_index[0]][current_index[1]]=='G':
            return 1
        elif board[current_index[0]][current_index[1]]=='R':
            continue
        else :
            queue.append({'loc':current_index,'value':1})
    while queue:
        current = queue.popleft()
        visited[str(current['loc'])]=1
        for i in range(4):
            next_index = [current['loc'][0]+UDLR_y[i],current['loc'][1]+UDLR_x[i]]
            while next_index[0]<len(board) and next_index[0]>-1 and next_index[1]<len(board[0]) and next_index[1]>-1 and board[next_index[0]][next_index[1]]!='D':
                next_index = [next_index[0]+UDLR_y[i],next_index[1]+UDLR_x[i]]
            current_index = [next_index[0]-UDLR_y[i],next_index[1]-UDLR_x[i]]
            if board[current_index[0]][current_index[1]]=='G':
                return current['value']+1
            elif str(current_index) in visited:
                continue
            else :
                queue.append({'loc':current_index,'value':current['value']+1})
    return -1