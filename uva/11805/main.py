import sys

input()
for i, line in enumerate(sys.stdin.readlines()):
    n, k, p = list(map(int, line.split()))
    k -= 1
    res = (k + p) % n
    print(f"Case {i + 1}: {res + 1}")
