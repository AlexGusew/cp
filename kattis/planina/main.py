n = int(input())
side = 2
for _ in range(n):
    side += side - 1
print(side**2)
