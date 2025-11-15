#!/usr/bin/python3
for i in range(0, 100):
    for j in range(i+1, 100):
        if i != 98:
            print("{:02d}, {:02d}".format(i, j), end=", ")
        else:
            print("{:02d}, {:02d}".format(i, j))
        break
