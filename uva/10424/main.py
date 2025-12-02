import sys

arr = []
for line in sys.stdin.readlines():
    arr.append(line)
    if len(arr) % 2:
        continue

    def calc(s):
        val = sum([ord(i.lower()) - ord("a") + 1 for i in s if i.isalpha()])
        while val >= 10:
            newVal = 0
            while val:
                newVal += val % 10
                val //= 10
            val = newVal
        return val

    a, b = calc(arr[0]), calc(arr[1])
    if a < b:
        a, b = b, a
    print(f"{b / a * 100:.2f} %")
    arr = []
