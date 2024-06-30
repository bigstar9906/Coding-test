def solution(x, n):
    answer = []
    x1 = x
    for i in range(n):
        answer.append(x1)
        x1+=x
    return answer