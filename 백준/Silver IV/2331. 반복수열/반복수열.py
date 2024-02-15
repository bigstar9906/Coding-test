from collections import Counter
A,P = map(int,input().split()) # 입력받기

dupl = Counter([]) # 중복된 수를 저장할 리스트
num = 0 # 중복된 수의 개수를 저장할 변수

while True:
  if A in dupl: # 만약 중복된 수가 나오면
    num = A
    break # 반복문을 종료한다
  dupl[A] = 1 # 중복된 수가 아니면 리스트에 추가한다
  A = sum([int(i)**P for i in str(A)]) # 각 자리수를 P제곱하여 더한다

print(list(dupl.keys()).index(num)) 

