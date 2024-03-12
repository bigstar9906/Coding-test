from collections import deque

def solution(scores):
    rank = deque()
    hash = dict()

    for score in scores:
        if len(rank) == 0:
            rank.append({
                "scores": [score],
                "minDoc": score[0],
                "maxDoc": score[0],
                "minInt": score[1],
                "maxInt": score[1]
            })
        else:
            plused = False
            i = 0
            while True:
                if i == len(rank):
                    break
                if (score[0] >= rank[i]["maxDoc"] and score[1] > rank[i]["maxInt"]) or ((score[0] > rank[i]["maxDoc"] and score[1] >= rank[i]["maxInt"])):
                    if not plused:
                        rank.insert(i, {
                            "scores": [score],
                            "minDoc": score[0],
                            "maxDoc": score[0],
                            "minInt": score[1],
                            "maxInt": score[1]
                        })
                        break
                elif not (score[0] <= rank[i]["minDoc"] and score[1] < rank[i]["minInt"]) and not (score[0] < rank[i]["minDoc"] and score[1] <= rank[i]["minInt"]):
                    if plused:
                        rank[i - 1]['scores'] += rank[i]["scores"][:]
                        rank[i - 1]["minDoc"] = min(rank[i - 1]["minDoc"], rank[i]["minDoc"])
                        rank[i - 1]["maxDoc"] = max(rank[i - 1]["maxDoc"], rank[i]["maxDoc"])
                        rank[i - 1]["minInt"] = min(rank[i - 1]["minInt"], rank[i]["minInt"])
                        rank[i - 1]["maxInt"] = max(rank[i - 1]["maxInt"], rank[i]["maxInt"])
                        rank.remove(rank[i])
                        i -= 1
                    else:
                        rank[i]["scores"].append(score)
                        rank[i]["minDoc"] = min(rank[i]["minDoc"], score[0])
                        rank[i]["maxDoc"] = max(rank[i]["maxDoc"], score[0])
                        rank[i]["maxInt"] = max(rank[i]["maxInt"], score[1])
                        rank[i]["minInt"] = min(rank[i]["minInt"], score[1])
                        plused = True
                elif i == len(rank) - 1 and plused == False:
                    rank.append({
                        "scores": [score],
                        "minDoc": score[0],
                        "maxDoc": score[0],
                        "minInt": score[1],
                        "maxInt": score[1]
                    })
                    break
                i += 1

    num = 1
    for r in rank:
        for s in r["scores"]:
            hash[str(s)] = num
        num += len(r['scores'])

    answer = []
    for score in scores:
        answer.append(hash[str(score)])

    return answer

if __name__ == "__main__":
    n = int(input())
    scores = []
    for i in range(n):
        scores.append(list(map(int, input().split())))
    print(solution(scores))