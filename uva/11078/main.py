from math import inf

for _ in range(int(input())):
    arr = [int(input()) for _ in range(int(input()))]
    sen = arr[0]
    res = -inf
    for val in arr[1:]:
        res = max(res, sen - val)
        sen = max(sen, val)
    print(res)
