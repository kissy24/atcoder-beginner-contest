n = int(input())
s = [input() for i in range(n)]

c = 0
a = ""
for i in list(set(s)):
    if c < s.count(i):
        c = s.count(i)
        a = i
print(a)
