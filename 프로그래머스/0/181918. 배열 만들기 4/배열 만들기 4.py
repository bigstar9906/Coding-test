def solution(arr):
    stk = []
    i = 0
    while len(arr)>i:
        if len(stk)==0:
            stk.append(arr[i])
            i+=1
        elif stk[-1]<arr[i]:
            stk.append(arr[i])
            i+=1
        else:
            del stk[-1]
    return stk