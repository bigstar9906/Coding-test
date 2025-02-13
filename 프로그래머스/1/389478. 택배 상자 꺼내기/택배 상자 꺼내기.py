def solution(n, w, num):
    return (n-1)//w - (num-1)//w + (1 if ((n-1)//w%2==(num-1)//w%2 and (n-1)%w>=(num-1)%w) or ((n-1)//w%2!=(num-1)//w%2 and (n-1)%w+(num-1)%w+2>w) else 0)