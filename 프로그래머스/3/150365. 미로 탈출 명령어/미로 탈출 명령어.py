# d->l->r->u
def solution(n, m, x, y, r, c, k):
    answer = ''
    diff = k - abs(c-y) - abs(r-x)
    if diff<0 or diff%2==1:
        return 'impossible'
    for i in range(r-x):
        answer+='d'
    canDown = min(diff//2,n-max(r,x))
    diff-=canDown*2
    for i in range(canDown):
        answer+='d'
    for i in range(y-c):
        answer+='l'
    canLeft = min(diff//2,min(c,y)-1)
    for i in range(canLeft):
        answer+='l'
    diff-=canLeft*2
    for i in range(diff//2):
        if min(c,y)-canLeft<m:
            answer+='rl'
        else:
            answer+='ud'
    for i in range(canLeft):
        answer+='r'
    for i in range(c-y):
        answer+='r'
    for i in range(canDown):
        answer+='u'
    for i in range(x-r):
        answer+='u'
    return answer