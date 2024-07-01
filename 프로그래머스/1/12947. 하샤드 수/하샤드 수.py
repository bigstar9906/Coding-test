def solution(x):
    return x%sum(int(item) for item in list(str(x)))==0