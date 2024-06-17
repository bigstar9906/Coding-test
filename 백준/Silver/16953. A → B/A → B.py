A,B = map(int,input().split())
answer = 0
while A!=B and A<B:
    if B%2 ==0:
        B = B//2
        answer += 1
    elif B%10 == 1:
        B = B//10
        answer += 1
    else:
        print(-1)
        exit()
if A==B:
    print(answer+1)
else:
    print(-1)
