import sys

case = 0
for n in sys.stdin:
    case += 1
    if int(n) == 0:
        break
    nums = list(map(int, input().split()))
    a = len([i for i in nums if i > 0])
    b = len([i for i in nums if i == 0])
    print(f"Case {case}: {a - b}")
