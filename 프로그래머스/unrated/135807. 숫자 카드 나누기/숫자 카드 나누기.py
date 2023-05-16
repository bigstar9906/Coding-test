def calcdpc(intA, intB):
    less = min(intA,intB)
    bigger = max(intA,intB)
    while bigger%less!=0:
        bigger -= less
        intA = bigger
        intB = less
        bigger = max(intA,intB)
        less = min(intA,intB)
        if bigger%2==1 and less == 2 : return 1
    return less
def solution(arrayA, arrayB):
    answers = [0]
    dpcA = arrayA[0]
    for i in range(1,len(arrayA)):
        dpcA = calcdpc(dpcA,arrayA[i])
    dpcB = arrayB[0]
    for i in range(1,len(arrayB)):
        dpcB = calcdpc(dpcB,arrayB[i])
    dpcAs = []
    dpcBs = []
    for i in range(1,dpcA+1):
        if dpcA%i==0: dpcAs.append(i)
    dpcAs.reverse()
    for i in range(1,dpcB+1):
        if dpcB%i==0: dpcBs.append(i)
    dpcBs.reverse()
    complete = 1
    for i in dpcBs:
        for j in range(0,len(arrayA)):
            if arrayA[j]%i==0:
                complete=0
                break
        if complete == 1 : 
            if i == 1 : answers.append(0)
            else :answers.append(i)
            break
    complete =1
    for i in dpcAs:
        for j in range(0,len(arrayB)):
            if arrayB[j]%i==0:
                complete=0
                break
        if complete == 1 : 
            if i == 1 : answers.append(0)
            else :answers.append(i)
            break
    return max(answers)