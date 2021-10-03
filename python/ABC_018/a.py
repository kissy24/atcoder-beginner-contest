A = int(input())
B = int(input())
C = int(input())

seq = [A, B, C]
seq_sorted = sorted([A, B, C], reverse=True)

for s in seq:
    if s == seq_sorted[0]:
        print(1)
    elif s == seq_sorted[1]:
        print(2)
    else:
        print(3)
