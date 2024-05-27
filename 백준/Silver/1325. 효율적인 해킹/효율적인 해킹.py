from collections import deque
n,m = map(int,input().split())
trust = dict()
for i in range(m):
    a,b = map(int,input().split())
    if b not in trust:
        trust[b] = []
    trust[b].append(a)
def bfs(start):
    num = 1
    q = deque()
    q.append(start)
    visited = [0]*(n+1)
    visited[start] = 1
    while q:
        x = q.popleft()
        if x in trust:
            for i in trust[x]:
                if visited[i] == 0:
                    visited[i] = 1
                    num+=1
                    q.append(i)
    return num
answer = []
max_num = 0
for i in sorted(trust):
    num = bfs(i)
    if num > max_num:
        max_num = num
        answer = [i]
    elif num == max_num:
        answer.append(i)
print(*answer)