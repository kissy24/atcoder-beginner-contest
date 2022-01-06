km = int(input()) / 1000

if km < 0.1:
    print("00")
elif km >= 0.1 and km <= 5:
    if km < 1:
        print(f"0{int(km * 10)}")
    else:
        print(f"{int(km * 10)}")
elif km >= 6 and km <= 30:
    print(f"{int(km + 50)}")
elif km >= 35 and km <= 70:
    print(f"{int((km -30)/5 +80)}")
else:
    print("89")

