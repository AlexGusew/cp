import sys

for i, line in enumerate(sys.stdin):
    vals = list(map(int, line.split()))[1:]
    print(f"Case {i + 1}: {min(vals)} {max(vals)} {max(vals) - min(vals)}")
