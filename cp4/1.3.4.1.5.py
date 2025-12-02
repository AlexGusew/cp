import random

dates = [
    (random.randint(0, 11), random.randint(0, 30), -random.randint(1950, 2025))
    for _ in range(10)
]
dates.sort()

print(*dates, sep="\n")
