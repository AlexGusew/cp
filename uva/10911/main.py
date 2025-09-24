import math

from math import inf, sqrt


def main():
    while True:
        n = int(input())
        if n == 0:
            break
        arr = []
        for _ in range(2 * n):
            _, x, y = input().split()
            arr.append((int(x), int(y)))
        print(arr)

        minVal = math.inf

        def dfs(seen, val):
            nonlocal minVal
            if len(seen) == 2 * n:
                minVal = min(minVal, val)
            for i in range(2 * n):
                if i in seen:
                    continue
                seen.add(i)
                for j in range(2 * n):
                    if j in seen:
                        continue
                    seen.add(j)
                    newVal = math.sqrt(
                        pow(arr[i][0] - arr[j][0], 2) + pow(arr[i][1] - arr[j][1], 2)
                    )
                    dfs(seen, val + newVal)
                    seen.remove(j)
                seen.remove(i)

        dfs(set(), 0)
        print(minVal)


main()
