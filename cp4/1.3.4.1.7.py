import math


chars = "abcdefghyj"
res = []


def dfs(used: set[str], path: list[str]):
    if len(path) == len(chars):
        res.append("".join(path))
    for char in chars:
        if char in used:
            continue
        used.add(char)
        path.append(char)
        dfs(used, path)
        used.remove(char)
        path.pop()


dfs(set(), [])

# print(res)
print(math.factorial(10), len(res))
