inStr = "3 + (8 - 7.5) * 10 / 5 - (2 + 5 * 7)"
s = inStr.replace("(", " ( ").replace(")", " ) ").split()
s.append(")")

val = 0
op = "+"
stack = ["("]

for i in range(len(s)):
    if s[i] in "+-":
        stack.extend([op, val])
        val = 0
        op = s[i]
    elif s[i] in "*/":
        op = s[i]
    elif s[i] == "(":
        stack.extend([op])
        val = 0
        op = "+"
    elif s[i] == ")":
        while stack and stack[-1] != "(":
            pval, pop = stack.pop(), stack.pop()
            if pop == "-":
                pval *= -1
            val += pval
    else:
        num = float(s[i])
        if op == "*":
            val *= num
        elif op == "/":
            val /= num
