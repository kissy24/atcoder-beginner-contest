n = int(input())
s = input()
word = "b"
a = -1


def check(word, s, a, a_):
    return a_ if word == s else a


a = check(word, s, a, 0)
for i in range(1, n + 1):
    if i % 3 == 1:
        word = f"a{word}c"
    elif i % 3 == 2:
        word = f"c{word}a"
    else:
        word = f"b{word}b"
    a = check(word, s, a, i)
print(a)
