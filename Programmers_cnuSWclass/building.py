n = int(input())
buildings = list(map(int, input().split()))
left, right = 1, 1
bL, bR = buildings[0], buildings[n-1]
for b in buildings:
    if b > bL:
        bL = b
        left += 1

for i in range(n-1, 0, -1):
    b = buildings[i]
    if b > bR:
        bR = b
        right += 1

print(left, right, sep=' ')
