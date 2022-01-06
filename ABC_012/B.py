import datetime as dt

d = str(dt.timedelta(seconds=int(input())))
list_ = d.split(":")
if len(list_[0]) < 2:
    list_[0] = f"0{list_[0]}"
print(f"{list_[0]}:{list_[1]}:{list_[2]}")
