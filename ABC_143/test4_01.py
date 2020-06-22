import bisect
N = int(input())
dlist = list(map(int, input().split()))
dlist.sort(reverse=True)

sum = 0
count_b = 0
count_c = 0
for a in range(N):
    count_b = count_b + 1
    for b in range(count_b, N):
        sum += bisect.bisect_left(dlist,dlist[a] - dlist[b]) 
print(sum)
