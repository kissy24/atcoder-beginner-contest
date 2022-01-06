n = int(input())

sum = 0
for i in range(n):
    sum += ((i + 1) * 10000) * (1 / n)

print(int(sum))
