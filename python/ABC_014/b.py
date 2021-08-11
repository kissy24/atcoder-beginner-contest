def main():
    n, X = map(int, input().split())
    a_seq = list(map(int, input().split()))
    price = 0
    bn = f"0{(bin(X))[2:]}"
    for i, b in enumerate(bn[::-1]):
        if int(b):
            price += a_seq[i]
    print(price)


if __name__ == "__main__":
    main()
