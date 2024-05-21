n,m = map(int,input().split())
medal = []
point = [-1]
characters = []
for i in range(n):
    split = input().split()
    if int(split[1]) == point[-1]:
        continue
    medal.append(split[0])
    point.append(int(split[1]))
for i in range(m):
    characters.append(int(input()))
for i in range(m):
    chara = characters[i]
    head = 0
    tail = len(point)
    mid = 0
    while head < tail:
        mid = (head+tail)//2
        if point[mid]<chara<=point[mid+1]:
            mid+=1
            break
        if point[mid]==chara:
            break
        if mid!=len(point)-1 and point[mid+1] < chara:
            head = mid+1
        else:
            tail = mid
    print(medal[mid-1])