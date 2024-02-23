def solution(name):
    answer = len(name)-1
    alpha =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in name:
        index = alpha.index(i)
        answer+= index if index<14 else 26-index
    A_positions = []
    if len(name)<2:
        return answer
    state = {'key':'isA','value':1,'index':1} if name[1]=='A'else {'key':'notA','value':1,'index':1}
    for i in range(2,len(name)):
        if name[i]=='A':
            if state['key'] == 'isA':
                state['value']+=1
            else :
                A_positions.append(state)
                state = {'key':'isA','value':1,'index':i}
        else :
            if state['key']=='notA':
                state['value']+=1
            else :
                A_positions.append(state)
                state = {'key':'notA','value':1,'index':i}
    A_positions.append(state)
    if A_positions[0]['key']=='isA' and A_positions[-1]['key']=='isA':
        shorter = max(A_positions[0]['value'],A_positions[-1]['value'])
        value = A_positions[0]['value']+A_positions[-1]['value']
        A_positions.sort(key=lambda x:(x['key'],-x['value']))
        if A_positions[0]['value']<value+1:
            return answer-shorter
    A_positions.sort(key=lambda x:(x['key'],-x['value']))
    A_position = A_positions[0]
    shorter = 0
    if A_position['key']=='isA':
        shorter = A_position['value']- min(A_position['index']-1,len(name)-A_position['index']-A_position['value'])
            
    if shorter>0:
        answer-=shorter
    return answer