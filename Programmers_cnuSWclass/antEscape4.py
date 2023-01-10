testCase = int(input())

'''
1
6 2
.O&#@#
.#@&#O
10 2
.O.#&#...@
11 3
O..##@###&.

3 0
O@O

12 5
O#####@#&##O

10 3
@#.#.#&#O.


10 50
100 8
'''
def crushWall(ant, wolrd, crush):
    print('***crushWall init***')
    i = ant
    start = ant-crush if ant-crush > 0 else 0
    print(f'start: {start}')
    while i > start:
        if world[i] == '#':
            del world[i]
        i -= 1
    print(world)


    ant = world.index('@')

    end = ant + crush if ant + crush < len(world) else len(world)
    print(f'end: {end}')
    while i <= end and i < len(world):
        if world[i] == '#':
            del wolrd[i]

    print(world)
    ant = world.index('@')
    return ant, world

def crushWalls(ant, world, crush, flag):
    if crush <= 0:
        return ant, world, crush

    else:
        if flag:
            for i in range(crush):
                if ant-1 >= 0 and world[ant-1] == '#':
                    del world[ant-1]
                    ant -= 1
                    crush -= 1
                    print(world)

        else:
            for i in range(crush):
                if ant+1 < len(world) and world[ant+1] == '#':
                    del world[ant+1]
                    crush -= 1
                    print(world)

        return ant, world, crush


def fightMonster(atk_ant, hp_ant, atk_m, hp_m):
    print('***fightMonster init***')
    flag = True
    while True:
        hp_m -= atk_ant
        if hp_m <= 0:
            break

        hp_ant -= atk_m
        if hp_ant <= 0:
            flag = False
            break

    return flag

def verifyEscafeLeft(ant, world):
    if world[ant - 1] == 'O':
        return 0

    elif world[ant - 1] == '#':
        return 1

    elif world[ant - 1] == '&':
        return 2

def verifyEscafeRight(ant, world):
    if world[ant + 1] == 'O':
        return 0  # 탈출

    elif world[ant + 1] == '#':
        return 1  # 벽깨기

    elif world[ant + 1] == '&':
        return 2  # 몬스터

def escafeWorld(ant, world, crush, flag_crush,atk_ant, hp_ant, atk_m, hp_m):
    flag = True
    ant, world, crush = crushWalls(ant, world, crush, flag_crush)
    answer = verifyEscafeLeft(ant, world)

    if answer == 0:
        flag = True

    elif answer == 1:
        flag = False

    elif answer == 2:
        flag2 = fightMonster(atk_ant, hp_ant, atk_m, hp_m)

        if flag2:
            world.remove('&')
            return escafeWorld(ant, world, crush, flag_crush, atk_ant, hp_ant, atk_m, hp_m)
        else:
            flag = False

    return flag



for test in range(testCase):
    length, crush = map(int, input().split())
    world = list( input().strip().replace('.', ''))
    ant = world.index('@')
    atk_ant, hp_ant = map(int, input().split())
    atk_m, hp_m = map(int, input().split())

    #왼쪽부터
    crush_l = crush
    flag = escafeWorld(ant, world, crush, True, atk_ant, hp_ant, atk_m, hp_m)

    if flag is False:
        flag = escafeWorld(ant, world, crush, False, atk_ant, hp_ant, atk_m, hp_m)

    if flag:
        print('HAHA!')
    else:
        print('HELP!')



    '''if ant != 0 and ant != len(world)-1:
        if (world[ant-1] != 'O' and world[ant+1] != 'O') and (world[ant-1] == '&' or world[ant+1] == '&'):
            flag = fightMonster(atk_ant, hp_ant, atk_m, hp_m)

    elif ant == 0:
        if world[ant+1] != 'O' and world[ant+1] == '&':
            flag = fightMonster(atk_ant, hp_ant, atk_m, hp_m)

    elif ant == len(world)-1:
        if world[ant-1] != 'O' and world[ant-1] == '&':
            flag = fightMonster(atk_ant, hp_ant, atk_m, hp_m)'''

    if flag:
        print('HAHA!')
    else:
        print('HELP!')

