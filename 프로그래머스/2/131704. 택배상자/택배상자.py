from collections import deque,Counter
def solution(order):
    boxes = deque(list(range(1,len(order)+1)))
    box_cnt = Counter(list(range(1,len(order)+1)))
    cover = deque()
    answer=0
    idx = 0
    while idx<len(order):
        i = order[idx]
        if len(boxes)>0 and i==boxes[0]:
            answer+=1
            boxes.popleft()
            box_cnt[i]-=1
            idx+=1
        elif box_cnt[i]==1:
            current = boxes.popleft()
            cover.append(current)
            box_cnt[current]-=1
        elif len(cover)>0 and i == cover[-1]:
            answer+=1
            cover.pop()
            idx+=1
        else:
            break
    return answer