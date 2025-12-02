for _ in range(int(input())):
    line = input()
    if line == "P=NP":
        print("skipped")
    else:
        a, b = map(int, line.split("+"))
        print(a + b)
