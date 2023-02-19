import decimal
context = decimal.getcontext()
context.rounding = decimal.ROUND_HALF_UP
def dropZero(num):
    num = str(num)
    if num[-1] == '0':
        print(num[:-1])
    else:
        print(num)
def kToM():
    for i in range(int(input())):
        case = input().split(' ')
        if case[1] == 'K':
            convert = round(decimal.Decimal(int(case[0])/1.6), 2)
            dropZero(convert)

        else:
            convert = round(decimal.Decimal(int(case[0])*1.6), 2)
            dropZero(convert)


# 배열의 최소합
def sumMins():
    arr = list(map(int, input().split(' ')))
    length = len(arr)
    target =[]
    i=1

    while i <= length and length > 1:
       arr = sorted(arr)
       n = arr[i-1] + arr[i]
       arr.append(n)
       target.append(n)
       del arr[i-1]
       del arr[i-1]
       length -= 1
    print(sum(target))

#프로그래밍
def calPolynomial():
    arr1 = list(map(int, input().split(' ')))
    arr2 = list(map(int, input().split(' ')))
    sumArr = []
    subArr = []
    for i in range(0, len(arr1), 2):
        sumItem = arr1[i] + arr2[i]
        subItem = arr1[i] - arr2[i]

        if subItem == 0 or sumItem == 0:
            pass
        else:
            sumArr.append(str(sumItem))
            sumArr.append(str(arr1[i+1]))
            subArr.append(str(subItem))
            subArr.append(str(arr1[i+1]))


    print(' '.join(sumArr))
    print(' '.join(subArr))

#뱀키우기
def moveSnake(start, command):
    if command == 'R':
        start[1] += 1
    elif command == 'L':
        start[1] -= 1
    elif command == 'U':
        start[0] -= 1
    elif command == 'D':
        start[0] -= 1
    return start

def snakeGame():
    width, height = map(int, input().split(' '))

    feed = []
    for i in range(int(input())):
        a, b = map(int, input().split(' '))
        feed.append((a,b))

    move = list(input().split())
    start = (0, 0)
    snakeLength = 0
    for i in move:
        start = moveSnake(start, i)
        if start in feed:
            snakeLength += 1


if __name__ == '__main__':
    # kToM()
    # sumMins()
    # calPolynomial()
    snakeGame()
