import sys
sys.setrecursionlimit(10000)
m,n,k = map(int,input().split())
maps = []
answer = []
size = 0
for i in range(m):
    maps.append([0]*n)
for i in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for x in range(x1,x2):
        for y in range(y1,y2):
            maps[y][x]=1
def bfs(x,y):
    if (not -1<x<n) or (not -1<y<m):
        return 0
    if maps[y][x]==1:
        return 0
    maps[y][x]=1
    return 1+bfs(x,y-1)+bfs(x,y+1)+bfs(x-1,y)+bfs(x+1,y)
for y in range(m):
    for x in range(n):
        current = bfs(x,y)
        if current:
            answer.append(current)
print(len(answer))
print(*sorted(answer))