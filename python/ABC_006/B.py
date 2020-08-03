n = int(input())

dp = [0, 0, 1]

for i in range(3, n):
    # 剰余算を組み込まないと桁溢れでTLE,MLEになる
    dp.append((dp[i - 1] + dp[i - 2] + dp[i - 3]) % 10007)

print(dp[n - 1])
