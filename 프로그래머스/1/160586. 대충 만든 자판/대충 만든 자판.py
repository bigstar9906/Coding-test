from collections import Counter
def solution(keymap, targets):
    fastKeys = Counter()
    for km in keymap:
        for idx in range(len(km)):
            if not fastKeys[km[idx]]:
                fastKeys[km[idx]] = idx+1
            else:
                fastKeys[km[idx]] = min(fastKeys[km[idx]],idx+1)
    answer = []
    for target in targets:
        num=0
        isBreak = False
        for letter in target:
            if letter in fastKeys:
                num+=fastKeys[letter]
            else:
                isBreak=True
                break
        if isBreak:
            answer.append(-1)
        else:
            answer.append(num)
    return answer