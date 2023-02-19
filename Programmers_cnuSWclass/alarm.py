#백준 2884, 알람맞추기
h, m = map(int, input().split())
m -= 45
if m<0:
    m += 60
    h -= 1

if h<0:
    h += 24

print(f'{h} {m}')