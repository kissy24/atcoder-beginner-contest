s = list(input())
n = int(input())
quotient = int(n / 5) if (remainder := n % 5) != 0 else int(n / 5) - 1
print(f"{s[quotient]}{s[remainder - 1]}")
