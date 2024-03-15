def solution(picks, minerals):
    answer = 0
    cnt = 0
    sets = []
    values = dict()
    values["diamond"] = 25
    values["iron"] = 5
    values["stone"] = 1
    left = -1
    for mine in minerals:
        if cnt%5==0:
            sets.append(0)
        sets[cnt//5]+=values[mine]
        cnt+=1
    if len(sets)>(picks[0]+picks[1]+picks[2]):
        sets = sets[:picks[0]+picks[1]+picks[2]]
    elif len(minerals)%5!=0:
        left = sets[-1]
        del sets[-1]
    
    sets.sort(reverse=True)
    for s in sets:
        if s<left:
            if picks[0]>0:                    
                answer+=left//25
                left %= 25
                answer += left//5
                left%= 5
                answer += left
                picks[0]-=1
            elif picks[1]>0:
                answer+=left//25*5
                left%=25
                answer+=left//5
                left%=5
                answer+=s
                picks[1]-=1
            elif picks[2]>0:
                answer+=left
                picks[2]-=1
            left=-1
        if picks[0]>0:
            if s==25:
                answer+=5
                picks[0]-=1
                continue
            if s==5:
                answer+=5
                picks[0]-=1
                continue
            answer+=s//25
            s %= 25
            answer += s//5
            s%= 5
            answer += s
            picks[0]-=1
        elif picks[1]>0:
            if s==5:
                answer+=5
                picks[1]-=1
                continue
            answer+=s//25*5
            s%=25
            answer+=s//5
            s%=5
            answer+=s
            picks[1]-=1
        elif picks[2]>0:
            answer+=s
            picks[2]-=1
    if left >0:
        if picks[0]>0:                    
            answer+=left//25
            left %= 25
            answer += left//5
            left%= 5
            answer += left
            picks[0]-=1
        elif picks[1]>0:
            answer+=left//25*5
            left%=25
            answer+=left//5
            left%=5
            answer+=left
            picks[1]-=1
        elif picks[2]>0:
            answer+=left
            picks[2]-=1
    return answer