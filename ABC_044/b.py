from collections import Counter

print(
    "No" if sum(map(lambda x: bool(x % 2), Counter(list(input())).values())) else "Yes"
)
