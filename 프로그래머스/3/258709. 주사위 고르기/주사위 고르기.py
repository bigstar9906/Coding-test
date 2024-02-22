from collections import Counter


def solution(dice):
    whole =  list(range(1,len(dice)+1))
    half = whole[:len(dice)//2]
    answer = []
    times = 1
    for i in range(len(dice)//2+1,len(dice)+1):
        times *=i
    for i in range(1,len(dice)//2+1):
        times = times//i
    times = times//2
#     len(dice) C 2 //2
    for i in range(times):
        a = {'key':half[:],'win':0,'draw':0,'loose':0}
        b = {'key':[],'win':0,'draw':0,'loose':0}
        b['key'] = whole[:]
        for j in half:
            b['key'].remove(j)
        
        
        count_a = Counter(dice[half[0]-1])
        for x in range(1,len(a['key'])):
            count_t = Counter(dice[half[x]-1])
            count_r = Counter()
            for y in list(count_a.keys()):
                for z in list(count_t.keys()):
                    count_r[y+z]+=count_a[y]*count_t[z]
            count_a = count_r
        count_b = Counter(dice[b['key'][0]-1])
        for x in range(1,len(b['key'])):
            count_t = Counter(dice[b['key'][x]-1])
            count_r = Counter()
            for y in list(count_b.keys()):
                for z in list(count_t.keys()):
                    count_r[y+z]+=count_b[y]*count_t[z]
            count_b = count_r
        for j in list(count_a.keys()):
            for k in list(count_b.keys()):
                temp = count_a[j]*count_b[k]
                if j>k:
                    a['win']+=temp
                    b['loose']+=temp
                elif j==k:
                    a['draw']+=temp
                    b['draw']+=temp
                else :
                    a['loose']+=temp
                    b['win']+=temp
        answer.append(a)
        answer.append(b)
        
        if half[-1]==len(whole):
            for index in range(1,len(half)):
                if half[-1-index] == len(whole)-index:
                    continue
                else :
                    half[-1-index]+=1
                    for idx in range(index):
                        half[-1-index+idx+1] = half[-1-index+idx]+1
                    break
                    
        else:
            half[-1]+=1
    answer.sort(key=lambda x:x['win'],reverse=True)
    return answer[0]['key']
    
    







     