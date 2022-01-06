from collections import Counter

n = int(input())
a = Counter(int(input()) for _ in range(n))
print(sum(a.values()) - len(a))
