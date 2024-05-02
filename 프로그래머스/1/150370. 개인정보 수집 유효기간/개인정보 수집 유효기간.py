def solution(today, terms, privacies):
    answer = []
    termInfo = dict()
    today = today.split('.')
    for term in terms:
        spl = term.split(" ")
        termInfo[spl[0]] = spl[1]
    for i in range(len(privacies)):
        spl = privacies[i].split(" ")
        date = spl[0].split(".")
        diff = (int(today[0]) - int(date[0]))*12 +int(today[1])-int(date[1])
        if int(today[2])-int(date[2])<0:
            diff-=0.5
        else:
            diff+=0.5
        print(diff)
        if diff>int(termInfo[spl[1]]):
            answer.append(i+1)
    return answer