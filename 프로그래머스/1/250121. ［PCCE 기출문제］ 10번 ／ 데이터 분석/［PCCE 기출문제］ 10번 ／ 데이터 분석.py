def solution(data, ext, val_ext, sort_by):
    answer = []
    idx =  dict()
    idx["code"] = 0
    idx["date"] = 1
    idx["maximum"] = 2
    idx["remain"] = 3
    for d in data:
        if d[idx[ext]]<val_ext:
            answer.append(d)
    answer.sort(key=lambda x:x[idx[sort_by]])
    return answer