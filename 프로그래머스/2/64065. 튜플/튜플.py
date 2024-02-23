from collections import Counter
def solution(s):
    s = s.replace('{','').replace('}','')
    numbers = Counter(s.split(',')).most_common()
    answer = []
    for number in numbers:
        answer.append(int(number[0]))
    return answer