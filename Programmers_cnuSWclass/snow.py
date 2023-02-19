n = int(input())
r1, c1, r2, c2 = map(lambda x: int(x)-1, input().split())

if c1 > c2:
    c1, c2 = c2, c1
if r1 > r2:
    r1, r2 = r2, r1

snow = ''
for i in range(n):
    s = ''
    for j in range(n):
        if r1 <= i <= r2:
            if c1 <= j <= c2:
                s += '.'

            else:
                s += '*'

        else:
            s += '*'
    snow += s+'\n'

print(snow.strip())