res = []
N = 20


def dfs(i, path):
    if i > N:
        res.append(path[:])
        return
    dfs(i + 1, path)
    path.append(i)
    dfs(i + 1, path)
    path.pop()


dfs(1, [])

print(res[:20])
