inputStr = [["FF", 16, 10], ["11111111", 2, 10]]
for s, base, tBase in inputStr:
    num = int(s, base)
    print(s, num, hex(num), oct(num), bin(num))
