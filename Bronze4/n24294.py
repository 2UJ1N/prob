#
# 24294
# ГРАДИНА
# https://www.acmicpc.net/problem/24294

import sys
input = sys.stdin.readline

w1 = int(input())
h1 = int(input())
w2 = int(input())
h2 = int(input())

print(4 + 2 * max(w1, w2) + 2 * (h1 + h2))