input()
line = input().split()

for i in range(len(line)):
    if line[i] != "mumble":
        p = int(line[i])
        if p != i + 1:
            print("something is fishy")
            break
else:
    print("makes sense")
