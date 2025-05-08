from collections import Counter
def solution(N, number):
    numbers =dict()
    cnt = Counter()
    for i in range(1,9):
        numbers[i] = [int(str([N]*i).replace("[","").replace("]","").replace(",","").replace(" ",""))]
        cnt[numbers[i][0]]+=1
        if numbers[i][0]==number:
            return i
        if i>1:
            for j in range(1,i//2+1):
                for n1 in numbers[i-j]:
                    for n2 in numbers[j]:
                        if cnt[n1*n2]==0:
                            cnt[n1*n2]+=1
                            numbers[i].append(n1*n2)
                        if cnt[n1+n2]==0:
                            cnt[n1+n2]+=1
                            numbers[i].append(n1+n2)
                        if cnt[abs(n1-n2)]==0 and abs(n1-n2) >1:
                            cnt[abs(n1-n2)]+=1
                            numbers[i].append(abs(n1-n2))
                        if cnt[n1//n2]==0 and n1%n2==0:
                            cnt[n1//n2]+=1
                            numbers[i].append(n1//n2)
            if number in numbers[i]:
                return i
        print(i,numbers[i])
    return -1