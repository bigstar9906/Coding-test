def solution(s):
    answer = True
    open_cnt = 0
    for x in s:
        if x =='(':
            open_cnt+=1
        elif open_cnt>0:
            open_cnt-=1
        else:
            return False
    return open_cnt==0