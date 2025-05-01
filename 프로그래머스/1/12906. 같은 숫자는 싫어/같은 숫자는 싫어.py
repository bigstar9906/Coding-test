def solution(arr):
    answer = []
    before = arr[0]
    for i in range(1,len(arr)):
        if arr[i]!=before:
            answer.append(before)
            before = arr[i]
    answer.append(before)
    return answer