import copy

W = input()

wlist = list(W)
wlist2 = copy.deepcopy(wlist)
boin = ["a", "i", "u", "e", "o"]

for w in wlist:
    for b in boin:
        if w == b:
            wlist2.remove(w)
print("".join(wlist2))
