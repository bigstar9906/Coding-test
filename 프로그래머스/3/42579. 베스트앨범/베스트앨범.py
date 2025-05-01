def solution(genres, plays):
    d = dict()
    answer=[]
    for i in range(len(genres)):
        if genres[i] not in d:
            d[genres[i]]={"songs":[{"key":i,"plays":plays[i]}],"sum":plays[i]}
        else:
            current = d[genres[i]]
            current["songs"].append({"key":i,"plays":plays[i]})
            current["sum"]+=plays[i]
    rank = sorted(d,key=lambda x: -d[x]["sum"])
    for genre in rank:
        songs = sorted(d[genre]["songs"],key=lambda x:-x["plays"])
        answer.append(songs[0]["key"])
        if len(songs)>1:
            answer.append(songs[1]["key"])
    return answer