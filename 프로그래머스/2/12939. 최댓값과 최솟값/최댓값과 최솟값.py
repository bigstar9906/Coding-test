def solution(s):
    max_val = 'null'
    min_val = 'null'
    for i in s.split(' '):
        num = int(i)
        if max_val=='null':
            max_val = num
            min_val = num
        else:
            max_val = max(max_val,num)
            min_val = min(min_val,num)
    return str(min_val)+" "+str(max_val)