import math

n = int(input())
a = 100000

for i in range(1, int(math.sqrt(n)) + 1):
    a = min(a, (n - (i * (n // i)) + abs(i - (n // i))))

print(a)
