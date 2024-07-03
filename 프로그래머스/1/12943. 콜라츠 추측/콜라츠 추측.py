def solution(num):
    step = 500
    while num>1 and step>0:
        if num%2==0:
            num/=2
        else:
            num = num*3+1
        step-=1
    if step>=1:
        return 500-step
    return -1
    