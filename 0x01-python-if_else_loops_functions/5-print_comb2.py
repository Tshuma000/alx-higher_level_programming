#!/usr/bin/python3
for i in range(0, 100):
    if i < 10:
        print("{}".format(f"{i:02}"), end= ", ")
    elif i == 99:
        print("99")
    else:
        print("{}".format(i), end=", ")