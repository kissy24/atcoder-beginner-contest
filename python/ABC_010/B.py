n = int(input())
a = list(map(int, input().split()))
c = 0
for j in a:
    if j > 2:
        c += j % 3

print(c)
