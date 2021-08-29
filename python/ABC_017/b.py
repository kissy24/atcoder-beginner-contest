N = int(input())
L_N = list(map(int, input().split(" ")))
L_max = sorted(L_N)[-1]
print("Yes" if sum(L_N) - L_max > L_max else "No")