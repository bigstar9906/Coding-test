
def extend(a):
    answer = a
    if len(a)==2:
        answer+=a
    else:
        for i in range(0,4-len(a)):
            answer+=min(a)
            
    if a[0]>a[len(a)-1]:
        answer+=str(4-len(a))
    elif a[0]<a[len(a)-1]:
        answer+=str(len(a))
    else:
        if len(a)>2:
            if a[0]> a[1]:
                answer+=str(len(a))
            else : answer+=str(4-len(a))
        else : answer+="0"
    return answer



def solution(numbers):
    answer = ""
    numbers.sort(key = lambda x:(extend(str(x))),reverse = True)
    for num in numbers:
        answer+= str(num)
    if max(answer)=="0": return "0"
    return answer