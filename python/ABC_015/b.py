from math import ceil

N = int(input())
A_N = list(map(int, input().split(" ")))
print(ceil(sum(A_N) / (N - A_N.count(0))))
