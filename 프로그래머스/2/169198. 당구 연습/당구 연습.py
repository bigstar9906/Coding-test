import math
def min_dist(white,black,m,n):
    result = []
    if white[0]!=black[0] or white[1]>black[1]:
        result.append(math.pow(white[0]-black[0],2)+ math.pow(white[1]-(2*n-black[1]),2))
    if white[0]!=black[0] or white[1]<black[1]:
        result.append(math.pow(white[0]-black[0],2)+ math.pow(white[1]-(black[1]*-1),2))
    if white[1]!=black[1] or white[0]>black[0]:
        result.append(math.pow(white[1]-black[1],2)+ math.pow(white[0]-(2*m-black[0]),2))
    if white[1]!=black[1] or white[0]<black[0]:
        result.append(math.pow(white[1]-black[1],2)+ math.pow(white[0]-(black[0]*-1),2))
        
    return min(result)
    
def solution(m, n, startX, startY, balls):
    answer = []
    for i in balls:
        answer.append(min_dist([startX,startY],i,m,n))
    return answer