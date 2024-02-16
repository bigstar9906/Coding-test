import sys

sys.setrecursionlimit(1000000)

def dfs(land,i,j,minmax):
    if i < 0 or j<0 or i>len(land)-1 or j>len(land[0])-1:
        return 0
    elif land[i][j] ==0:
        return 0
    else :
        land[i][j] = 0
        minmax[0] = min(minmax[0],j)
        minmax[1] = max(minmax[1],j)
        return dfs(land,i+1,j,minmax)+ dfs(land,i-1,j,minmax)+dfs(land,i,j+1,minmax)+dfs(land,i,j-1,minmax)+1

def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    answer = [0]*len(land[0])
    for col in range (0,m):
        for row in range(0,n):
            minmax = [col,col]
            value = dfs(land,row,col,minmax)
            if value!=0:
                for x in range(minmax[0],minmax[1]+1):
                    answer[x]+=value        
    return max(answer)