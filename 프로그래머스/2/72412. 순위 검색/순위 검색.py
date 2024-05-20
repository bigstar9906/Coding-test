from itertools import combinations
def solution(info, query):
    infos = dict()
    infos_sorted = dict()
    answer = []
    infos[str(answer)] = []
    infos_sorted[str(answer)] = False
    for i in info:
        i = i.split(" ")
        score = i.pop()
        infos[str(answer)].append(score)
        for j in range(1,5):
            for attr in combinations(i,j):
                attr = str(list(attr))
                if attr in infos:
                    infos[attr].append(score)
                else:
                    infos[attr] = [score]
                    infos_sorted[attr] = False
    for q in query:
        q = q.split(" ")
        option = []
        result = 0
        for idx in range(0,7,2):
            if q[idx] != '-':
                option.append(q[idx])
        if str(option) in infos:
            if not infos_sorted[str(option)]:
                infos_sorted[str(option)]=True
                infos[str(option)] = sorted(infos[str(option)],key=lambda x:int(x))
            arr = infos[str(option)]
            start = 0
            end = len(arr)-1
            found = -1
            while start<=end:
                mid = (start+end)//2
                if int(arr[mid])>=int(q[7]) and (mid==0 or int(arr[mid-1])<int(q[7])):
                    found = mid
                    break
                elif int(arr[mid])>=int(q[7]):
                    end = mid-1
                else:
                    start=mid+1
            if found == -1:
                answer.append(0)
            else:
                len_info = len(infos[str(option)])
                answer.append(len_info-found)
        else:
            answer.append(0)
    return answer