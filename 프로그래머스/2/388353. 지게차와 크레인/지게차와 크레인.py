from collections import deque
blocks = []

def bfs(i,j,n,m):
    buffer = deque()
    buffer.append([i,j])
    while len(buffer)>0:
        current = buffer.popleft()
        blocks[current[0]][current[1]]='0'
        if current[0]!=0 and blocks[current[0]-1][current[1]]=='1':
            buffer.append([current[0]-1,current[1]])
        if current[0]!=n-1 and blocks[current[0]+1][current[1]]=='1':
            buffer.append([current[0]+1,current[1]])
        if current[1]!=0 and blocks[current[0]][current[1]-1]=='1':
            buffer.append([current[0],current[1]-1])
        if current[1]!=m-1 and blocks[current[0]][current[1]+1]=='1':
            buffer.append([current[0],current[1]+1])
        

def solution(storage, requests):
    n=len(storage)
    m=len(storage[0])
    for i in range(n):
        blocks.append(list(storage[i]))
    answer = n*m
    for r in requests:
        current = []
        if len(r)==2:
            for i in range(n):
                for j in range(m):
                    if blocks[i][j]==r[0]:
                        if (i==0 or i==n-1 or j==0 or j==m-1 or 
                                blocks[i-1][j]=='0' or blocks[i+1][j]=='0' or
                                blocks[i][j-1]=='0' or blocks[i][j+1]=='0'):
                            bfs(i,j,n,m)
                        else:
                            current.append([i,j])
                        answer-=1
            for c in current:
                blocks[c[0]][c[1]]='1'
                if not (c[0]==0 or c[0]==n-1 or c[1]==0 or c[1]==m-1) and (blocks[c[0]-1][c[1]]=='0' or
                                                                          blocks[c[0]+1][c[1]]=='0' or
                                                                          blocks[c[0]][c[1]-1]=='0' or
                                                                          blocks[c[0]][c[1]+1]=='0'):
                    bfs(c[0],c[1],n,m)
        else:
            for i in range(n):
                for j in range(m):
                    if blocks[i][j]==r and (i==0 or i==n-1 or j==0 or j==m-1 or
                                            blocks[i-1][j]=='0' or blocks[i+1][j]=='0' or
                                            blocks[i][j-1]=='0' or blocks[i][j+1]=='0'):
                        current.append([i,j])
            for c in current:
                bfs(c[0],c[1],n,m)
                answer-=1      
    return answer