import bisect
N=int(input())
L=sorted(list(map(int,input().split())))
print(L)
ans=0
for i in range(N-2):
  print(i)
  for j in range(i+1,N-1):
    ans+=bisect.bisect_left(L,L[i]+L[j])-j-1 # Code 1 
    # ans+=bisect.bisect_left(L,L[i]+L[j],j)-j-1 # Code 2 
#print(ans)