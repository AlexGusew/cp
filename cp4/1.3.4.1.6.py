import random
import bisect

arr = [random.randint(4, 100000) for _ in range(10**6)]

arr.sort()

idx = bisect.bisect_left(arr, 3)
print(arr[idx] == 3)
print(arr[:40])
