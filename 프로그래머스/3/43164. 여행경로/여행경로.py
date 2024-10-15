from copy import deepcopy
def dfs(city,cities,depth,n):
    answer = []
    if depth==n:
        return [city]
    if city not in cities or cities[city]==[]:
        return ["000"]
    for destination in cities[city]:
        refl = deepcopy(cities)
        refl[city].remove(destination)
        for ans in dfs(destination,deepcopy(refl),depth+1,n):
            if ans !="000":
                answer.append(city+" "+ans)
    return answer
        
        
        

def solution(tickets):
    answer = ["ICN"]
    cities = dict()
    # 티켓 정보 수집
    for ticket in tickets:
        if ticket[0] in cities:
            cities[ticket[0]].append(ticket[1])
        else:
            cities[ticket[0]]=[ticket[1]]
    return sorted(dfs("ICN",cities,0,len(tickets)))[0].split(" ")
    