A, B, C = map(int, input().split(" "))

if A + B == C and A - B == C:
    out = "?"
elif A + B != C and A - B == C:
    out = "-"
elif A + B == C and A - B != C:
    out = "+"
else:
    out = "!"


print(out)
