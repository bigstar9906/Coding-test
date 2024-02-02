def solution(s):
    past =  []
    for i in range(len(s)):
        if past and past[-1] == s[i]:
            del past[len(past)-1]
        else:
            past.append(s[i])
    return 0 if past else 1