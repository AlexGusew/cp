import sys

x = int(input())
n = int(input())

val = (n + 1) * x

for line in range(n):
    a = int(input())
    val -= a

print(val)
