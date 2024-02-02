def solution(n):
    fibo = [0,1]
    for i in range(1,n):
        result = fibo[i-1]+fibo[i]
        if result>1234566:
            result %= 1234567
        fibo.append(result)
    return fibo[n]