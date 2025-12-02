import math

for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    x = math.ceil((a - 2) / 3) * math.ceil((b - 2) / 3)
    print(x)
