'''n, m = map(int, input().split())
adj = [[] for i in range(n)]
print(adj)
for i in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    adj[u][v], adj[v][u] = 1, 1

s = ""
for l in adj:
    if not l:
        l.append(-1)
    s += ' '.join(list(map(str, sorted(l)))) + '\n'
print(s)'''



n, m = map(int, input().split())
adj = [[] for i in range(n)]
print(adj)
for i in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    adj[u].append(v+1)
    adj[v].append(u+1)

s = ""
for l in adj:
    if not l:
        l.append(-1)
    s += ' '.join(list(map(str, sorted(l)))) + '\n'
print(s)
