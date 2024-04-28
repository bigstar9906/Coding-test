from collections import Counter
def solution(topping):
    answer=0
    head = 0
    tail = len(topping)-1
    head_cnt = Counter()
    tail_cnt = Counter()
    head_cnt[topping[head]]+=1
    tail_cnt[topping[tail]]+=1
    while head<tail-1:
        if len(head_cnt)>len(tail_cnt):
            tail-=1
            tail_cnt[topping[tail]]+=1
        else:
            head+=1
            head_cnt[topping[head]]+=1
    if len(head_cnt)==len(tail_cnt):
        while len(head_cnt)==len(tail_cnt):
            answer+=1
            head_cnt[topping[head]]-=1
            if head_cnt[topping[head]]==0:
                del head_cnt[topping[head]]
            tail_cnt[topping[head]]+=1
            head-=1
    else:
        while len(head_cnt)>len(tail_cnt):
            head_cnt[topping[head]]-=1
            if head_cnt[topping[head]]==0:
                del head_cnt[topping[head]]
            tail_cnt[topping[head]]+=1
            head-=1
        while len(head_cnt)==len(tail_cnt):
            answer+=1
            head_cnt[topping[head]]-=1
            if head_cnt[topping[head]]==0:
                del head_cnt[topping[head]]
            tail_cnt[topping[head]]+=1
            head-=1
    return answer