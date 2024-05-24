start,end = map(int, input().split())
now = 1
prev = 0
idx = 1
while now<start:
    prev=now
    now +=idx+1
    idx+=1
answer = (min(now,end)-start+1)*idx
while now<end:
    prev=now
    now +=idx+1
    idx+=1
    answer += (min(now,end)-max(start,prev))*idx
print(answer)