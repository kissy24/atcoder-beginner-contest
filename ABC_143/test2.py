N = int(input())

dlist=list(map(int, input().split()))

sum = 0
count = 1

for d in dlist:
    for i in range(count,N):
        sum = sum + dlist[i]*d
    count = count + 1 

print(sum)