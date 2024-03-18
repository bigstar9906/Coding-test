def solution(priorities, location):
    answer = 1
    while True:
        prior = max(priorities)
        idx = priorities.index(prior)
        if idx==location:
            return answer
        elif idx<location:
            location -= idx+1
        else :
            location = len(priorities)-idx+location-1
        del priorities[idx]
        priorities = priorities[idx:]+priorities[:idx]
        answer+=1
    