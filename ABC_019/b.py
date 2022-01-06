s = list(input())

A = ""
count = 1
for i in range(len(s)):
    if i == 0:
        continue
    if s[i - 1] == s[i]:
        count += 1
    else:
        A += f"{s[i-1]}{count}"
        count = 1
else:
    A += f"{s[i]}{count}"

print(A)
