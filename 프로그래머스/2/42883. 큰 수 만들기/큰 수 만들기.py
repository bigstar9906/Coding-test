def solution(number, k):
    answer = ""
    answer_len = len(number)-k
    for n in number:
        if k<1:
            answer+=n
        else:
            plused = False
            for i in range(int(n)-1,-1,-1):
                if str(i) in answer:
                    idx = answer.index(str(i))
                    skip = len(answer)-idx
                    if k>=skip:
                        k-=skip
                        if idx ==0:
                            answer = ""
                        else :
                            answer = answer[:idx]
                        answer+=n
                        plused = True
                        break
                    else :
                        answer = answer[:len(answer)-k]
                        answer+=n
                        plused = True
                        k=0
                        break
            if not plused:
                if len(answer)<answer_len:
                    answer+=n
                else :
                    k-=1
    return answer