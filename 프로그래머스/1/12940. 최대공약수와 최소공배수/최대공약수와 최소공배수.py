import math
from collections import Counter
def analyze(num):
    origin =num
    divider = []
    i=2
    while num!=1 and i<math.sqrt(origin)+2:
        if num%i==0:
            divider.append(i)
            num=num//i
        else:
            i+=1
    if len(divider)==0:
        divider.append(origin)
    elif num!=1:
        divider.append(num)
    return Counter(divider)

def solution(n, m):
    if n==1 or m==1:
        return [1,n*m]
    n_div = analyze(n)
    m_div = analyze(m)
    intersection =n_div&m_div
    union = n_div|m_div
    print(n_div,m_div,intersection,union)
    inter = 1
    for key in intersection.keys():
        inter=inter*pow(key,intersection[key])
    uni = 1
    for key in union.keys():
        uni=uni*pow(key,union[key])
    return [inter,uni]
        