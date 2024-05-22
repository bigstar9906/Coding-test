from itertools import combinations
n=1
while n>0:
    lst = list(map(int, input().split()))
    n = lst[0]
    arr = lst[1:]
    for i in combinations(arr,6):
        print(' '.join(map(str,i)))
    print()