for i in range(int(input())):
    length = int(input())
    umm = input()
    a, b = map(int, input().split())

    umm = umm[a-1:b]
    if 'Umm' in umm and umm.count('U') == 1 and umm.startswith('U'):
        print('YES')
    else:
        print('NO')
