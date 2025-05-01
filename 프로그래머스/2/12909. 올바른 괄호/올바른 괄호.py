def solution(s):
    answer = True
    open_cnt = 0
    for l in s:
        open_cnt += 1 if l=="(" else -1
        if open_cnt<0:
            return False
    return open_cnt==0