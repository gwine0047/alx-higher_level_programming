#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if i != j:
            if j > i:
                if i == 8 and j == 9:
                    print('89')
                else:
                    print("{}{}, ".format(i, j), end="")
