n= int(input())
answer = 0
start = '0123456789'
end = '9876543210'

isPossible = True
for i in range(0,n):
  ans_str = str(answer)
  for j in range(0,len(ans_str)):
      if j==len(ans_str)-1:
          answer+=1
      else:
          current = ans_str[j]
          if ans_str[j+1:]==end[end.index(current)+1:end.index(current)+len(ans_str)-j]:
            if j==0 and current=='9':
                answer = int(start[:len(ans_str)+1][::-1])
                break
            else:
                answer = int(ans_str[0:j]+ str(int(current)+1)+ start[:len(ans_str)-j-1][::-1])
                break
  if answer==int(end) and i!=n-1:
      isPossible = False
      break

if isPossible :
    print(answer)
else: 
    print(-1)