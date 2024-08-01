from collections import deque
def solution(maps):
    answer=[]
    visited = []
    directions = [[0,1],[0,-1],[1,0],[-1,0]]
    rows = len(maps)
    cols = len(maps[0])
    for i in range(rows):
        visited.append([0]*cols)
    for row in range(rows):
        for col in range(cols):
            if maps[row][col]!='X' and visited[row][col]==0:
                val = int(maps[row][col])
                visited[row][col]=1
                queue = deque()
                for d in directions:
                    currentRow = row+d[0]
                    currentCol = col+d[1]
                    if currentRow>-1 and currentRow<rows and currentCol>-1 and currentCol<cols and maps[currentRow][currentCol]!='X' and visited[currentRow][currentCol]==0:
                        queue.append([currentRow,currentCol])
                while len(queue)>0:
                    current = queue.popleft()
                    if maps[current[0]][current[1]]!='X' and visited[current[0]][current[1]]==0:
                        val+=int(maps[current[0]][current[1]])
                        visited[current[0]][current[1]]=1
                        for d in directions:
                            currentRow = current[0]+d[0]
                            currentCol = current[1]+d[1]
                            if currentRow>-1 and currentRow<rows and currentCol>-1 and currentCol<cols and maps[currentRow][currentCol]!='X' and visited[currentRow][currentCol]==0:
                                queue.append([currentRow,currentCol])
                answer.append(val)
    if len(answer)==0:
        return [-1]
    return sorted(answer)