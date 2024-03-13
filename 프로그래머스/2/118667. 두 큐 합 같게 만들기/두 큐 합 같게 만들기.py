from collections import deque
def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)
    answer = 0
    count = 0
    if sum1 == sum2:
        return 0
    for i in range(len(q1)*3):
        if sum1 > sum2:
            x = q1.popleft()
            q2.append(x)
            sum1 -=x
            sum2 +=x
            count+=1
            if sum1 == sum2:
                answer = count
                break;
        else:
            x = q2.popleft()
            q1.append(x)
            count+=1
            sum1+=x
            sum2-=x
            if sum1 == sum2:
                answer = count
                break;
            
    if answer != 0:
        return answer
    return -1