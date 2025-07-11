from itertools import permutations
def solution(k, dungeons):
    answer = -1
    for schedule in permutations(dungeons,len(dungeons)):
        current = k
        goes = 0
        for dungeon in schedule:
            needs = dungeon[0]
            cost = dungeon[1]
            if current>=dungeon[0]:
                goes+=1
                current-=cost
        answer = max([answer,goes])
    return answer