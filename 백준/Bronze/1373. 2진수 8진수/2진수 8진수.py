from collections import deque
n=input()
stack = 0
digit = 1
num = 0
answer = deque()
not0 = False
for i in range(len(n)-1,-1,-1):
    if stack==3:
        if num!=0:
            not0=True
        answer.appendleft(str(num))
        digit=1
        stack = 0
        num=0
    num += int(n[i])*digit
    digit *= 2
    stack += 1
if num!=0:
   answer.appendleft(str(num))
if not0:
    print(''.join(answer))
else :
    print(0)