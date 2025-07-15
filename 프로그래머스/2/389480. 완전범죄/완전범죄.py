import copy
def solution(info, n, m):
    dp=[]
    for i in range(len(info)+1):
        line = [n]*m
        dp.append(copy.deepcopy(line))
    dp[0][0]=0
    for i in range(1,len(info)+1):
        a=info[i-1][0]
        b=info[i-1][1]
        for j in range(m):
            dp[i][j]=min([dp[i][j],dp[i-1][j]+a])
            if j+b<m:
                dp[i][j+b]=min([dp[i][j+b],dp[i-1][j]])
    answer = n
    for i in range(m):
        answer = min([answer,dp[len(info)][i]])
    return -1 if answer>=n else answer