from collections import Counter
def solution(edges):
    answer = [0,0,0,0]
    head = Counter([])
    tail = Counter([])
    goto = dict()
    #삽입 노드 판별을 위한 Counter -> Edge의 Head인 경우는 많으면서 동시에 Tail인 경우는 없는 노드가 삽입 노드
    for edge in edges:
        head[edge[0]]+=1
        tail[edge[1]]+=1
        if edge[0] in goto:
            temp = goto[edge[0]]
            temp.append(edge[1])
            goto[edge[0]] = temp
        else :
            goto[edge[0]]= [edge[1]]
    heads = head.most_common()# Head인 경우가 많은 순서대로 -> 기존 노드의 경우 Head인 경우가 3개 이상일 수 없음.
    for h in heads:
        if tail[h[0]]==0:
            answer[0] = h[0]
            break
    #삽입 노드와 연결되어 있는 기존 노드 찾기
    nodes = goto[answer[0]]
    for node in nodes:
        #노드 순회 이전에 판단할 수 있는 것 판단
        if head[node]==0 or tail[node] ==0: #삽입 노드를 제외했을 때, 기존 노드가 연결이 끊어진 상태 -> 막대 그래프
            answer[2]+=1
        elif head[node]==2 : # 기존 노드가 연결이 2개인 상태 -> 8형 그래프
            answer[3]+=1
        else:
            rotate = False
            current = node
            while current!=node or rotate==False:
                rotate = True
                current = goto[current][0]
                if head[current]==0:
                    answer[2]+=1
                    break
                elif head[current]==2:
                    answer[3]+=1
                    break
            if current==node:
                answer[1]+=1
    return answer