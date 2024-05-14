from collections import Counter
from copy import deepcopy
def solution(n, wires):
    val = [1]*n
    wire_lst = []
    for w in wires:
        wire_lst+=w
        cnt = Counter(wire_lst)
    while max(cnt.values())!=len(wires):
        val_prev = deepcopy(val)
        for w in wires[:]:
                if cnt[w[0]]==1:
                    if val_prev[w[0]-1]!=max(val_prev) or val_prev.count(val_prev[w[0]-1])>1:
                        val[w[1]-1]+=val[w[0]-1]
                        val[w[0]-1]=0
                        wires.remove(w)
                elif cnt[w[1]]==1:
                    if val_prev[w[1]-1]!=max(val_prev) or val_prev.count(val_prev[w[1]-1])>1:
                        val[w[0]-1]+=val[w[1]-1]
                        val[w[1]-1]=0
                        wires.remove(w)
        wire_lst = []
        for w in wires:
            wire_lst+=w
            cnt = Counter(wire_lst)
    # if len(wires)==2:
    #     answer = []
    #     for i in Counter(wires[0]+wires[1]).keys():
    #         answer.append(val[i-1])
    #     return abs(max(answer)- sum(answer)+max(answer))
    if len(wires)==1:
        return abs(val[wires[0][0]-1]-val[wires[0][1]-1])
    else:
        answer = []
        root = cnt.most_common()[0][0]
        wires_sum = []
        for w in wires:
            wires_sum+=w
        for i in Counter(wires_sum).keys():
            if i!=root:
                answer.append(val[i-1])
        return abs(max(answer)- sum(answer)+max(answer)-val[root-1])
        