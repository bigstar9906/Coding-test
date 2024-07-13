from collections import Counter
def solution(id_list, report, k):
    answer = []
    cnt = Counter(report)
    user_cnt = Counter()
    mail_list = dict()
    for i in cnt.keys():
        report_info = i.split(" ")
        if report_info[1] in mail_list:
            mail_list[report_info[1]].append(report_info[0])
            if len(mail_list[report_info[1]])==k:
                for i in range(k):
                    user_cnt[mail_list[report_info[1]][i]]+=1
            elif len(mail_list[report_info[1]])>k:
                user_cnt[report_info[0]]+=1
        else :
            mail_list[report_info[1]] = [report_info[0]]
            if k==1:
                user_cnt[report_info[0]]+=1
    for user in id_list:
        answer.append(user_cnt[user])
    return answer