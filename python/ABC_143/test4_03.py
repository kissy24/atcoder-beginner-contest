N = int(input())
dlist = list(map(int, input().split()))
dlist.sort(reverse=True)
sum = 0

count_b = 0
count_c = 0
for a in range(N):
    count_b += 1
    count_c = count_b
    for b in range(count_b, N):
        count_c += 1 
        for c in range(count_c, N):
            if dlist[a] < dlist[b] + dlist[c]:
                sum += 1
            else:
                break
print(sum)