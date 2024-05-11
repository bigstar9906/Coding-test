def solution(s, n):
    answer = ""
    for c in s:
        c = ord(c)
        if c in range(97,123):
            answer+=chr((c+n)%123%97+97)
        elif c in range(65,91):
            answer+=chr((c+n)%91%65+65)
        else:
            answer+=' '
    return answer