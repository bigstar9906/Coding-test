def solution(genres, plays):
    answer = []
    play_count = dict()
    play_rank = dict()
    for i in range (len(genres)):
        if genres[i] in play_count:
            play_count[genres[i]]+=plays[i]
            for idx in range(len(play_rank[genres[i]])):
                if play_rank[genres[i]][idx]['count']<plays[i]:
                    play_rank[genres[i]].insert(idx,{'idx':i,'count':plays[i]})
                    break
                if idx == len(play_rank[genres[i]])-1:
                    play_rank[genres[i]].append({'idx':i,'count':plays[i]})
            if len(play_rank[genres[i]])>2:
                        play_rank[genres[i]].pop()
                    
        else:
            play_count[genres[i]]=plays[i]
            play_rank[genres[i]] = [{'idx':i,'count':plays[i]}]
    play_count = sorted(play_count.items(),key=lambda item:item[1],reverse=True)
    for play in play_count:
        for song in play_rank[play[0]]:
            answer.append(song['idx'])
    return answer