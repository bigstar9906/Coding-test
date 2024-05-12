def solution(a, b):
    dates = [31,29,31,30,31,30,31,31,30,31,30,31]
    today = sum(dates[0:a-1])+b-1
    days = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    return days[today%7]