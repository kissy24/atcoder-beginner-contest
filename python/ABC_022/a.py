n, s, t = map(int, input().split())
w = int(input())
a = [int(input()) for _ in range(n - 1)]
c = 0
for a_ in a:
    w += a_
    if w >= s and w <= t:
        c += 1
print(c)
