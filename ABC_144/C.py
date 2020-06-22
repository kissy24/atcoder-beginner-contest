N = int(input())
ans = 0

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

N_list = make_divisors(N)
if len(N_list) % 2 == 1:
    odd = len(N_list) / 2 
    i = N_list[int(odd)]
    ans = (i - 1)*2
else:
    even = len(N_list) / 2
    i = N_list[int(even) - 1]
    j = N_list[int(even)]
    ans = i+j-2

print(ans)