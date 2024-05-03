from itertools import product
import math
def solution(users, emoticons):
    answer = []
    for infos in list(product('1234',repeat=len(emoticons))):
        plus = 0
        sales = 0
        for user in users:
            idx =0
            temp =0
            for info in infos:
                if int(info)>=math.ceil(user[0]/10):
                    temp+=emoticons[idx]/10*(10-int(info))
                idx+=1
            if int(temp)>=user[1]:
                plus+=1
            else:
                sales+=int(temp)
        answer.append([plus,sales])
    return sorted(answer,key=lambda x:(x[0],x[1]),reverse=True)[0]