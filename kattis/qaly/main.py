import sys

val = 0
for line in range(int(input())):
    a, b = list(map(float, input().split()))
    val += a * b

print(val)
