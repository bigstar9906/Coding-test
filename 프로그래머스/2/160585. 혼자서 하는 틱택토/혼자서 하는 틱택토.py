def solution(board):
    answer = 1
# 순서의 오류가 발생한 경우
    CountO=0
    CountX=0
    for i in range(9):
        if board[i//3][i%3]=='O':
            CountO+=1
        if board[i//3][i%3]=='X':
            CountX+=1
    if CountX>CountO or CountO-CountX>1:
        answer = 0
#종료 조건을 달성하고도 계속 진행한 경우
    lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    Olines = []
    Xlines = []
    for line in lines:
        oneline = []
        for point in line:
            oneline.append(board[point//3][point%3])
        if oneline==["O","O","O"]:
            Olines.append(line)
        elif oneline==["X","X","X"]:
            Xlines.append(line)
    if len(Olines)==1 and (len(Xlines)>0 or CountX>CountO-1):
        answer=0
    elif len(Olines)==2 and len(set(Olines[0]).intersection(Olines[1]))==0:
        answer=0
    elif len(Xlines)==1 and CountO>CountX:
        answer=0
    elif len(Xlines)==2 and len(set(Xlines[0]).intersection(Xlines[0]))==0:
        answer=0
    return answer