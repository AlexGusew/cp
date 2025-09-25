import math, itertools

from itertools import product
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

        def dist(i, j):
            return sqrt(pow(arr[i][0] - arr[j][0], 2) + pow(arr[i][1] - arr[j][1], 2))

        n *= 2
        dp = [None] * 2**n
        dp[-1] = 0

        def dfs(mask):
            if dp[mask] is not None:
                return dp[mask]
            val = inf
            for i in range(n):
                if (1 << i) & mask:
                    continue
                for j in range(i + 1, n):
                    if (1 << j) & mask:
                        continue
                    val = min(dist(i, j) + dfs(mask | 1 << i | 1 << j), val)
            dp[mask] = val
            return val

        print(dfs(0))


main()
