n = int(input())
money = list(map(int, input().split()))


for m in money:
    less, more = 0, 0
    for i in money:
        if m > i:
            less += 1
        elif m < i:
            more += 1
    print(less, more, sep=' ')