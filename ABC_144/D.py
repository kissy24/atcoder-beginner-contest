import math

L=list(map(int, input().split()))
a = L[0]
b = L[1]
x = L[2]

l = x / (a**2)
c = 2*l - b
d = b - c
print(b)
print(l)
print(c)
print(d)
print(math.degrees(math.tan(float(d/a))))