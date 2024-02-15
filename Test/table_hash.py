def solution(data, col, row_begin, row_end):
    s = []
    sorted_data = sorted(data,key=lambda x: (x[col-1],-x[0]))
    for i in range(row_begin,row_end+1):
        s.append(0)
        for j in range(0,len(sorted_data[i-1])):
            s[i-row_begin]+=sorted_data[i-1][j]%i
    answer = s[0]
    for k in range(1,len(s)):
        answer = answer^s[k]
    return answer