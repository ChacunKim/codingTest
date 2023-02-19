n = int(input())
arr = list(map(int, input().split()))

if min(arr) == max(arr):
    print(0)
else:
    small = min(arr)
    for i in range(n):
        arr[i] -= small
    print(sum(arr))
