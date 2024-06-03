def solution(board, h, w):
    n = len(board)
    answer=0
    udlr = [[0,1],[0,-1],[1,0],[-1,0]]
    for i in udlr:
        cur = [h+i[0],w+i[1]]
        if not (-1<cur[0]<n) or not (-1<cur[1]<n):
            continue
        if board[cur[0]][cur[1]]==board[h][w]:
            answer+=1
    return answer