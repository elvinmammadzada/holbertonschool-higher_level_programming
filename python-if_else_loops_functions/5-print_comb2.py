#!/usr/bin/python3
for i in range(0, 100*100):
    a = i // 100
    b = i % 100
    if a < b:
        if a == 98 and b == 99:
            print("{:02d}, {:02d}".format(a, b))
        else:
            print("{:02d}, {:02d}".format(a, b), end=", ")

