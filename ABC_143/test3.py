N = int(input())
S = input()

len = 0
for i in range(N):
    if i < N:
        if S[i:i+1] != S[i+1:i+2]:
            len = len + 1
print(len)
