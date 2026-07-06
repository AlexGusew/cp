import math

for _ in range(int(input())):
    input()
    nums = list(map(int, input().split()))
    first = second = 0
    done = math.inf
    for i in range(len(nums)):
        first += (nums[i] == 1) - (nums[i] > 1)
        if done < i:
            second += (nums[i] < 3) - (nums[i] == 3)
        if done is not math.inf and second >= 0 and i < len(nums) - 1:
            print("yes")
            break
        if first >= 0:
            done = i
        if done is not math.inf and not first:
            second = 0
    else:
        print("no")

"""
1 3 3 1 1
  i
first = 0
second = -1
done = inf

1 1 3 3 1
  i
f = 1
s = 1


"""
