def solution(n, words):
    answer = []
    char = ''
    for word in words:
        if(word in answer or (False if char=='' else word[0]!=char) ):
            return [len(answer)%n+1,len(answer)//n+1]
        answer.append(word)
        char = word[-1]

    return [0,0]