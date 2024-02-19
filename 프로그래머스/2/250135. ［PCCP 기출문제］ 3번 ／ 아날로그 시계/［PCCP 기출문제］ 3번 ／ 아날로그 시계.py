def solution(h1, m1, s1, h2, m2, s2):
    #회전 수
    h_times = (h2-h1)//12
    m_times = (h2-h1)
    s_times = (h2-h1)*60+(m2-m1)
   #회전 각도
    s_rad = s_times*360+(s2-s1)*6
    m_rad = m_times*360+(m2-m1)*6+(s2-s1)*0.1
    h_rad = h_times*360+((h2-h1)%12)*30+(m2-m1)*0.5+(s2-s1)*0.5/60
    
    m_s = (s1*6-(m1*6+s1*0.1))+s_rad-m_rad if m1*6+s1*0.1>s1*6 else (s1*6-(m1*6+s1*0.1+360))+s_rad-m_rad
    h_s = (s1*6-(h1*30+m1*0.5+s1*0.5/60))+s_rad-h_rad if h1*30+m1*0.5+s1*0.5/60>s1*6 else (s1*6-(h1*30+m1*0.5+s1*0.5/60+360))+s_rad-h_rad
    
    m_s_times = m_s//360+1
    h_s_times = h_s//360+1
    
    answer = m_s_times + h_s_times
    
    if h2>11 and h1<12:
        answer-=1
    
    if s1*6==m1*6+s1*0.1:
        answer+=1
    if s1*6==h1*30+m1*0.5+s1*0.5/60:
        answer+=1
    if s1*6==m1*6+s1*0.1==h1*30+m1*0.5+s1*0.5/60:
        answer-=1
    
    
    
    return answer