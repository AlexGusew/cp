import random

n = 20
arr = [random.randint(1, 10) for _ in range(n)]
arr = [random.random() for _ in range(n)]
arr.sort()

print(*arr, sep="\n")
