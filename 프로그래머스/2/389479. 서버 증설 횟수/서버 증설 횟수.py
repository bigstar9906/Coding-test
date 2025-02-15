def solution(players, m, k):
    answer=0
    schedule = dict()
    current = 0
    idx = 0
    for player in players:
        if idx in schedule:
            current-=schedule[idx]
        if player>=(current+1)*m:
            answer+=player//m-current
            schedule[idx+k]=player//m-current
            current = player//m
        idx+=1
    return answer