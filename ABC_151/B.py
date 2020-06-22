nkm = list(map(int, input().split()))
N = nkm[0]
K = nkm[1]
M = nkm[2]

A = list(map(int, input().split()))

sum = N * M
rsum = 0
for i in A:
    rsum += i
sa = sum - rsum
if sa > K:
    print(-1)
elif sa < 0:
    print(0)
else:
    print(sa)
