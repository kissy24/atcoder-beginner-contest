def main():
    snack = int(input())
    children = int(input())
    extra_snack: int = snack % children
    add_snack = 0
    if extra_snack:
        add_snack = children - extra_snack
    print(add_snack)


if __name__ == "__main__":
    main()
