n = int(input())
arr = list(map(int, input().split()))
for i in range(len(arr)):
    arr[i] = abs(arr[i] - 320)

print(arr.index(min(arr))+1)
