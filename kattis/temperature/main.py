X, Y = map(int, input().split())
if Y == 1:
    if X == 0:
        print("ALL GOOD")
    else:
        print("IMPOSSIBLE")
else:
    print(X / (1 - Y))

import bisect
