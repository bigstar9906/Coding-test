from collections import Counter
def solution(participant, completion):
    answer = []
    complete = Counter(completion)
    runners = Counter(participant)
    for runner in participant:
        if runner not in complete :
            return runner
        elif runners[runner]!=complete[runner]:
            return runner
    