N = int(input())
ans = ''

for i in range(1,10):
    for j in range(1,10):
        if N == i*j:
            ans = 'Yes'
if ans == '':
    ans = 'No'
print(ans)
