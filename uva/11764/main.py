for case in range(int(input())):
    input()
    nums = list(map(int, input().split()))
    h = l = 0
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] > 0:
            h += 1
        elif nums[i] - nums[i - 1] < 0:
            l += 1
    print(f"Case {case + 1}: {h} {l}")
