n = int(input())
arr = list(map(int, input().split()))
num = max(arr)
for i in range(n):
    tmp = 0
    for j in range(i, n):
        tmp += arr[j]
        if tmp > num:
            num = tmp

print(num)
