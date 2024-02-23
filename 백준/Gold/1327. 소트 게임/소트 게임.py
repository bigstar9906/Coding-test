from collections import Counter, deque
N,K = map(int,input().split())
line = list(map(int,input().split()))

visited = Counter()
queue = deque()
step = 1

if sorted(line) == line:
    print(0)
else :
    for i in range(N-K+1):
        reversed = line[:i] + line[i:i+K][::-1] + line[i+K:]
        queue.append((reversed,step))
        visited[str(line)] = 1
    
    def bfs(N,K,line):
        while queue:
            line,step = queue.popleft()
            if sorted(line) == line:
                return step
            for i in range(N-K+1):
                reversed = line[:i] + line[i:i+K][::-1] + line[i+K:]
                if not visited[str(reversed)]:
                    queue.append((reversed,step+1))
                    visited[str(reversed)] = 1
        return -1
        
        
        
    print(bfs(N,K,line))