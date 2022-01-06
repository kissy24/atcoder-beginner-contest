L=list(map(int, input().split()))
A=L[0]
B=L[1]

ans=0
if A<=9:
    if B<=9:
        ans=A*B
    else:
        ans=-1
else:
    ans=-1

print(ans)