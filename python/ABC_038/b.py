hw1 = list(map(int, input().split()))
hw2 = list(map(int, input().split()))
hw = set(hw1 + hw2)
print("YES" if len(hw) != len(set(hw1)) + len(set(hw2)) else "NO")
