def solution(bandage, health, attacks):
    answer = health
    index = 0
    band_cnt = 0
    for i in range(attacks[0][0],attacks[len(attacks)-1][0]+1):
        if i==attacks[index][0]:
            band_cnt = 0
            answer-=attacks[index][1]
            if answer <1 :
                return -1;
            else :
                index+=1
        else :
            if answer<health:
                answer+=bandage[1]
                band_cnt+=1
                if band_cnt ==bandage[0]:
                    band_cnt = 0
                    answer+=bandage[2];
                if answer>health:
                    answer=health            
    return answer