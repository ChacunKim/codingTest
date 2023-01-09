len = int(input())
arr = list(map(int, input().strip().split()))
qNum = int(input())

for i in range(qNum):
    result = 0
    a, b = map(int, input().strip().split())
    a -= 1
    if a == b:
        print(arr[a])
    else:
        for idx in range(a, b):
            result += arr[idx]
    print(result)
