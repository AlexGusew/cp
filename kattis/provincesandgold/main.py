a, b, c = map(int, input().split())
res = a * 3 + b * 2 + c
vic = tre = ""

if res >= 8:
    vic = "Province"
elif res >= 5:
    vic = "Duchy"
elif res >= 2:
    vic = "Estate"

if res >= 6:
    tre = "Gold"
elif res >= 3:
    tre = "Silver"
elif res >= 0:
    tre = "Copper"

if vic:
    print(f"{vic} or {tre}")
else:
    print(tre)
