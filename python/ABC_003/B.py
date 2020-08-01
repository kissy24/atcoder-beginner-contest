import sys

# a = ["a", "t", "c", "o", "d", "e", "r", "@"] にして@の時だけ探索が思考的に一番簡単っぽい

s = list(input())
t = list(input())

a = ["a", "t", "c", "o", "d", "e", "r"]

for i in range(len(s)):
    if s[i] == t[i]:
        continue
    else:
        if s[i] == "@":
            if t[i] not in a:
                print("You will lose")
                sys.exit()
            else:
                continue
        if t[i] == "@":
            if s[i] not in a:
                print("You will lose")
                sys.exit()
            else:
                continue
        print("You will lose")
        sys.exit()

print("You can win")
