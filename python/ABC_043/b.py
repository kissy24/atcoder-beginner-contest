s = list(input())

a = ""
for _s in s:
    if _s == "1":
        a += "1"
    elif _s == "0":
        a += "0"
    else:
        a = a[:-1]
print(a)
