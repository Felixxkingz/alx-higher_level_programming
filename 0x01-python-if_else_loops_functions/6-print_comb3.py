#!/usr/bin/python3
for m in range(9):
    for n in range(10):
        if m < n:
            if ((m*10) + n) != 89:
                print("{}{}".format(m, n), end=", ")
            else:
                print("{}{}".format(m, n))
