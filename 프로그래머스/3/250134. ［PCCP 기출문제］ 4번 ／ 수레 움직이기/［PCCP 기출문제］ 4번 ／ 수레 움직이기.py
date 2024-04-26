from collections import deque
import copy
def solution(maze):
    red = []
    blue = []
    redExit = []
    blueExit = []
    fourward = [[0,-1],[0,1],[1,0],[-1,0]]
    n = len(maze)
    m  = len(maze[0])
    redVisit = copy.deepcopy(maze)
    blueVisit = copy.deepcopy(maze)
    for i in range(n):
        for j in range(m):
            here = maze[i][j]
            redVisit[i][j]=0
            blueVisit[i][j]=0
            if here==1:
                redVisit[i][j]=1
                red = [i,j]
            if here ==2:
                blueVisit[i][j]=1
                blue = [i,j]
            if here ==3:
                redExit = [i,j]
            if here ==4:
                blueExit = [i,j]
            if here ==5:
                redVisit[i][j]=1
                blueVisit[i][j]=1
    stack = deque()
    unit = {"red":red,"blue":blue,"redVisit":redVisit,"blueVisit":blueVisit,"ans":0}
    stack.append(unit)
    while(len(stack)>0):
        unit = stack.popleft()
        curRed = copy.deepcopy(unit["red"])
        curBlue = copy.deepcopy(unit["blue"])
        rCanMove = []
        for direct in fourward:
            if curRed==redExit:
                if curBlue ==blueExit:
                    return unit["ans"]
                rCanMove=[{"red":copy.deepcopy(curRed),"redVisit":copy.deepcopy(unit["redVisit"])}]
                continue
            newRed = [curRed[0]+direct[0],curRed[1]+direct[1]]
            if newRed[0] in range(n) and newRed[1] in range(m) and unit["redVisit"][newRed[0]][newRed[1]]!=1 and (newRed!=curBlue or curBlue!=blueExit):
                newRedVisit = copy.deepcopy(unit["redVisit"])
                newRedVisit[curRed[0]][curRed[1]] = 1
                rCanMove.append({"red":copy.deepcopy(newRed),"redVisit":copy.deepcopy(newRedVisit)})
        for r in rCanMove:
            if curBlue==blueExit:
                if curRed==redExit:
                    return unit["ans"]
                else:
                    stack.append({"red":copy.deepcopy(r["red"]),"blue":copy.deepcopy(curBlue),"redVisit":copy.deepcopy(r["redVisit"]),"blueVisit":copy.deepcopy(unit["blueVisit"]),"ans":unit["ans"]+1})
                    continue
            for direct in fourward:
                newBlue = [curBlue[0]+direct[0],curBlue[1]+direct[1]]
                if newBlue ==r["red"]:
                    continue
                if curBlue==r["red"] and newBlue==curRed:
                    continue
                if newBlue[0] in range(n) and newBlue[1] in range(m) and unit["blueVisit"][newBlue[0]][newBlue[1]]!=1:
                    newBlueVisit = copy.deepcopy(unit["blueVisit"])
                    newBlueVisit[curBlue[0]][curBlue[1]] = 1
                    newUnit = {"red":copy.deepcopy(r["red"]),"blue":copy.deepcopy(newBlue),"redVisit":copy.deepcopy(r["redVisit"]),"blueVisit":copy.deepcopy(newBlueVisit),"ans":unit["ans"]+1}
                    stack.append(newUnit)
    return 0