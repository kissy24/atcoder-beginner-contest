_ = int(input())
ab = list(map(int, input().split(" ")))
_ = int(input())
p = list(map(int, input().split(" ")))

print("YES" if len(set(nodes := p + ab)) == len(nodes) else "NO")
