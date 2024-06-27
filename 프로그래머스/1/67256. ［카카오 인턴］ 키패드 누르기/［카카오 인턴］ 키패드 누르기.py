def solution(numbers, hand):
    answer = ''
    left = 3
    right = 3
    l_num = [1,4,7]
    r_num = [3,6,9]
    m_num = [2,5,8,0]
    left_m = 1
    right_m = 1
    current = ''
    for num in numbers:
        if num in l_num:
            current = 'L'
            left_m=1
            left = l_num.index(num)
        elif num in r_num:
            current = 'R'
            right_m=1
            right = r_num.index(num)
        else:
            idx = m_num.index(num)
            diff = abs(idx-left)+left_m - abs(idx-right)-right_m
            if diff<0:
                left_m = 0
                current = 'L'
                left = idx
            elif diff>0:
                right_m = 0
                current = 'R'
                right = idx
            elif hand=='left':
                left_m = 0
                current = 'L'
                left = idx
            else :
                right_m = 0
                current = 'R'
                right = idx
        answer = ''.join([answer,current])
    return answer