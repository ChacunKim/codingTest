n = int(input())
arr = list(map(int, input().split()))
num = 0
li = []
for i in range(n):
    num += arr[i]
    li.append(num)

print(" ".join(map(str, li)))