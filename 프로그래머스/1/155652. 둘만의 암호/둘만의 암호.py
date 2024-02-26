def solution(s, skip, index):
    answer = ""
    skip = list(skip)
    skip.sort()
    for alpha in s:
        for i in range(index):
            alpha = chr(((ord(alpha)+1)%97)%26+97)
            while alpha in skip:
                alpha = chr(((ord(alpha)+1)%97)%26+97)
        
        answer+=alpha
    return answer