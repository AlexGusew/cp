from collections import Counter

for _ in range(int(input())):
    _, k = map(int, input().split())
    nums = list(map(int, input().split()))
    counter = Counter(nums)

    values = list(counter.values())
    values.append(0)
    values.sort()
    total = sum(values)
    res = 0
    n = len(values) - 1
    for i in range(1, len(values)):
        # print(
        #     "k = ",
        #     k,
        #     "nums = ",
        #     nums,
        #     "; values = ",
        #     values,
        #     "; i = ",
        #     i,
        #     "; total = ",
        #     total,
        # )
        if k >= total and (k - total) % (n - i + 1) == 0:
            res += 1
        total -= (values[i] - values[i - 1]) * (n - i + 1)
        if not total:
            break
    print(res)

"""
1 1 2 2 -> 5
0 2 2
  i
total = 4
res = 0
n = 2

0 1 2 -> 1
  i
total = 3
n = 2
"""
