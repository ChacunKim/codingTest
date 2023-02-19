#구간합으로 다시 풀어보기..
n = int(input())
weight = list(map(int, input().split()))

s = -1
for i in range(n):
    a = sum(weight[:i])
    b = sum(weight[i+1:])
    if a == b:
        s = i + 1

print(s)