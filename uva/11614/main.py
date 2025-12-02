import sys
import math


for _ in range(int(input())):
    n = int(sys.stdin.readline())
    r = (-1 + math.sqrt(1 + 8 * n)) // 2
    print(int(r))

"""

n - total amount
rows - not given

1 + 2 + .. + rows = n

rows - ?

(1 + r) / 2 * r = n
r^2 + r - 2n = 0

x = -b +- sqrt(b^2 - 4ac) / 2a
x = (-1 + (1 + 8n)) / 2

"""
