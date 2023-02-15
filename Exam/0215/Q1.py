a, b = map(int, input().split())
#b가 더 큰 것을 가정
if a > b :
    a, b = b, a
cnt, diff = 0,0
if a==b:
    pass

elif (a+b) % 2 == 0:

    while True:
        if a == b:
            break
        else:
            b -= 1
            a += 1
            cnt += 1

else:
    while True:
        if (b-a) == 1:
            break
        else:
            b -= 1
            a += 1
            cnt += 1
    diff = 1

print(diff, cnt, sep=' ')