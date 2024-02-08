n,m,v = map(int,input().split())
node = []
for i in range(m):
  node.append(list(map(int,input().split())))
node.sort(key=lambda x: (x[0]+x[1]))
visited = [False] * (n+1)
def dfs(node, v, visited):
  visited[v] = True
  print(v,end=' ')
  for i in range(0,m):
    if node[i][0]==v and not visited[node[i][1]]:
      dfs(node,node[i][1],visited)
    elif node[i][1]==v and not visited[node[i][0]]:
      dfs(node,node[i][0],visited)
  return

def bfs(node, v, visited):
  queue = [v]
  visited[v] = True
  while queue:
    v = queue.pop(0)
    print(v,end=' ')
    for i in range(0,m):
      if node[i][0]==v and not visited[node[i][1]]:
        queue.append(node[i][1])
        visited[node[i][1]] = True
      elif node[i][1]==v and not visited[node[i][0]]:
        queue.append(node[i][0])
        visited[node[i][0]] = True
  return
dfs(node,v,visited)
visited = [False] * (n+1)
print()
bfs(node,v,visited)