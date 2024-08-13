def solution(n, arr1, arr2):
    for i in range(n):
        arr1[i] = bin(arr1[i]|arr2[i]).split('0b')[1].zfill(n).replace("1","#").replace("0"," ")
    return arr1