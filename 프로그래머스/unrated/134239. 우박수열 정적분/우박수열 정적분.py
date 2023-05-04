def solution(k, ranges):
    answer = []
    res = k;
    prev_res =res;
    integ = []
    while res>1:
        if res%2==0:
            res = res/2;
        else :
            res = 3*res + 1;
        integ.append((res+prev_res)/2);
        prev_res = res;
    for i in range(0,len(ranges)):
        range_i = ranges[i][0];
        range_e = len(integ)+ranges[i][1];
        if range_i>range_e:
            answer.append(-1);
        elif range_i == range_e:
            answer.append(0);
        else :
            answer_integ = 0;
            for j in range(range_i,range_e):
                answer_integ+=integ[j];
            answer.append(answer_integ);
            
        
    return answer