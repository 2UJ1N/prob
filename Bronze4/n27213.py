#
# 27213
# Граничные клетки
# https://www.acmicpc.net/problem/27213

m = int(input())
n = int(input())

if m <= 3 or n <= 3:
    print(m * n)
else:
    print(2 * m + 2 * (n - 2))