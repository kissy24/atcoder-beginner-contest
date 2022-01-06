n, t = map(int, input().split())
seq = [int(input()) for _ in range(n)]
diff = sum(map(lambda a, b: t - (a - b) if a - b < t else 0, seq[1:], seq))
print(n * t - diff)
