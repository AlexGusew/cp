import math

abs(1 - 2)
for _ in range(int(input())):
    n = int(input())

    x = ((n * 567 / 9) + 7492) * 235 / 47 - 498
    if abs(x) < 10:
        print("0")
    else:
        x = abs(int(x)) // 10
        print(x % 10)
