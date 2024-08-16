def solution(n):
    return int(str(sorted(str(n),reverse=True)).replace("[","").replace("'","").replace("]","").replace(",","").replace(" ",""))