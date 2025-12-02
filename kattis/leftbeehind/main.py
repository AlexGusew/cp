import sys

for line in sys.stdin.readlines():
    if line == "0 0\n":
        break
    sw, so = map(int, line.split())
    if so + sw == 13:
        print("Never speak again.")
    elif so > sw:
        print("Left beehind.")
    elif so < sw:
        print("To the convention.")
    elif so == sw:
        print("Undecided.")
