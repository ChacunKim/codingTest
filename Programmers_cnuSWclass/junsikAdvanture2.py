for test in range(int(input())):
    n, m = map(int, input().split())
    world = []
    row, col = 0, 0
    damage = 0
    for i in range(n):
        w = list(input())
        world.append(w)

        if '@' in w:
            row, col = i, w.index('@')
            world[row][col] = '.'

    k = int(input())
    userInput = list(input())

    now = '.'
    for command in userInput:
        # print(row, col, sep=', ')
        if command == 'L' and col > 0:
            if world[row][col-1] == '.':
                col -= 1
                now = '.'
            elif world[row][col-1] == '^':
                col -= 1
                damage += 1
                now = '^'
            elif world[row][col-1] == '#' and now == '^':
                damage += 1

        elif command == 'R' and col < m-1:
            if world[row][col+1] == '.':
                col += 1
                now = '.'
            elif world[row][col+1] == '^':
                col += 1
                damage += 1
                now = '^'
            elif world[row][col+1] == '#' and now == '^':
                damage += 1

        elif command == 'U' and row > 0:
            if world[row-1][col] == '.':
                row -= 1
                now = '.'
            elif world[row-1][col] == '^':
                row -= 1
                damage += 1
                now = '^'
            elif world[row-1][col] == '#' and now == '^':
                damage += 1

        elif command == 'D' and row < n-1:
            if world[row+1][col] == '.':
                row += 1
                now = '.'
            elif world[row+1][col] == '^':
                row += 1
                damage += 1
                now = '^'
            elif world[row+1][col] == '#' and now == '^':
                damage += 1

    print(f'{row+1} {col+1} {damage}')

