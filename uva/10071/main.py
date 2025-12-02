import sys

for line in sys.stdin.readlines():
    v, t = map(int, line.split())
    print(v * 2 * t)
