def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        indices = [len(tree)]*26
        idx = 0
        for s in tree:
            indices[ord(s)-65] = idx
            idx+=1
        idx = -1
        isValid = True
        for s in skill:
            if idx>indices[ord(s)-65]:
                isValid=False
                break
            else:
                idx = indices[ord(s)-65]
        if isValid:
            answer+=1
    return answer