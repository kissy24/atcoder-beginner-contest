a = list(input())
b = list(input())
c = list(input())


def play(player: str):
    print(player.upper()) if not len(e := eval(player)) else play(e.pop(0))


play(a[0])
