for _ in range(int(input())):
    input()
    nums = list(map(int, input().split()))
    acc = sum(a > 1 for a in nums)
    if acc >= 2 or any(num > 2 for num in nums):
        print("yes")
    else:
        print("no")
