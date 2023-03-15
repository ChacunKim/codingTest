n, m = map(int, input().split())
arr = [[] for i in range(n)]
print(arr)
for i in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    arr[u].append(v)
    arr[v].append(u)

