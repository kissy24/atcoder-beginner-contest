n = int(input())
k = int(input())
x = int(input())
y = int(input())

print(k * x + (n - k) * y if n - k > 0 else n * x)
