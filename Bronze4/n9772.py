#
# 9772
# Quadrants
# https://www.acmicpc.net/problem/9772

import sys
input = sys.stdin.readline

while 1:
    x, y = map(float, input().split())

    if x == 0 and y == 0:
        print("AXIS")
        exit()
    elif x == 0 or y == 0:
        print("AXIS")
    elif x > 0:
        if y > 0:
            print("Q1")
        else:
            print("Q4")
    else:
        if y > 0:
            print("Q2")
        else:
            print("Q3")