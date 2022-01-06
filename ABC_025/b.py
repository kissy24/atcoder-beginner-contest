n, a, b = map(int, input().split())
sd = [input().split() for i in range(n)]
result = 0


def vector(s, d: int) -> int:
    return d * -1 if s == "East" else d


for s, d in sd:
    if (d_ := int(d)) < a:
        result += vector(s, a)
    elif d_ > b:
        result += vector(s, b)
    else:
        result += vector(s, d_)

if result > 0:
    print(f"West {result}")
elif result < 0:
    print(f"East {result * -1}")
else:
    print("0")
