n, m = map(int, input().split())
cups = [f'{i}' for i in range(1, n+1)]

for i in range(m):
    u, v = map(lambda x: int(x)-1, input().split())
    cups[u], cups[v] = cups[v], cups[u]

print(' '.join(cups))