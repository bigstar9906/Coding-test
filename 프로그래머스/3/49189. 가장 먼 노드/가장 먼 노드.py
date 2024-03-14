from collections import Counter
def solution(n, edge):
    nodes = dict()
    visited = Counter()
    visited[1] = 1
    for e in edge:
        if not e[0] in nodes:
            nodes[e[0]] = Counter()
        nodes[e[0]][e[1]] =1
        if not e[1] in nodes:
            nodes[e[1]] = Counter()
        nodes[e[1]][e[0]] = 1
    if not 1 in nodes:
        return 0
    else:
        next_dot = list(nodes[1])
        for dot in next_dot:
            visited[dot] = 1
        while True:
            next_next_dot = []
            for dot in next_dot:
                if dot in nodes:
                    for d in list(nodes[dot]):
                        if visited[d]==0:
                            next_next_dot.append(d)
                            visited[d]=1
            if len(next_next_dot)==0:
                return len(next_dot)
            next_dot = next_next_dot
                    
