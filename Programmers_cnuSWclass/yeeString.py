n, m = map(int, input().split())
s = input()
for i in range(m):
    l, r = map(int, input().split())
    print(s[l-1:r].count("e"))
