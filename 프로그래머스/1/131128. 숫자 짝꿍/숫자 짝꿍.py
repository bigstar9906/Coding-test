from collections import Counter
def solution(X, Y):
    X_CNT = Counter(X)
    Y_CNT = Counter(Y)
    answer = ''
    for i in range(9,-1,-1):
        i_in_Y = Y_CNT[str(i)]
        i_in_X = X_CNT[str(i)]
        if i_in_Y and i_in_X:
            answer = ''.join([answer,str(i)*min(i_in_Y,i_in_X)])
    if answer=='':
        return "-1"
    if answer[0]=='0':
        return "0"
    return answer