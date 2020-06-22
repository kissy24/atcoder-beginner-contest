A,B=map(int, input().split()) 
answer = A - 2*B
if answer < 0:
  answer = 0
 
print(answer)