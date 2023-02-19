for i in range(int(input())):
    n, m, k = map(int, input().split())
    prices = list(map(int, input().split()))

    stockPrice = prices[k-1]
    result = (False, 0)
    for idx in range(k, n):
        if prices[idx] >= stockPrice + m:
            result = (True, idx+1)
            break

    if result[0] is True:
        print(result[1])
    else:
        print("JB")
