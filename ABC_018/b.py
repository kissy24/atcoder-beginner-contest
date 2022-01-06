S = input()
N = int(input())

lrn = [list(map(int, input().split(" "))) for i in range(N)]

for lr in lrn:
    old_parts = S[lr[0] - 1 : lr[1]]
    new_parts = "".join(list(old_parts)[::-1])
    S = f"{S[:lr[0] - 1]}{new_parts}{S[lr[1]:]}"


print(S)
