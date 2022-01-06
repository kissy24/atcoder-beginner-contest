s = list(input())
a = ""
for i, j in enumerate(s):
    if i == 0:
        a += j.upper()
    else:
        a += j.lower()
print(a)
