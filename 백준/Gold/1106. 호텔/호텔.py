C,N = map(int,input().split())
cities = []
for i in range(N):
    a,b = map(int,input().split())
    cities.append([a,b])
Costs = dict()
cities.sort(key=lambda x: x[1]/x[0],reverse=True)

def min_cost(C,N,cities,Costs):
    minimum = (C//cities[0][1]+1)*cities[0][0]
    for city in cities:
        if C<=city[1]:
            minimum = min(minimum,city[0])
        for times in range(1,C//city[1]):
            if C == city[1]*times:
                minimum = min(minimum,city[0]*times)
            else:
                if (C-city[1]*times) in Costs:
                    minimum = min(minimum,city[0]*times+Costs[C-city[1]*times])
                else:
                    minimum = min(minimum,city[0]*times+min_cost(C-city[1]*times,N,cities,Costs))
    Costs[C] = minimum
    return minimum

print(min_cost(C,N,cities,Costs))