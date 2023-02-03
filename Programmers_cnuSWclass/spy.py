for i in range(int(input())):
    length = int(input())
    arr = list(map(int, input().split()))

    for item in arr:
        if arr.count(item) == 1:
            print(arr.index(item)+1)
            break
