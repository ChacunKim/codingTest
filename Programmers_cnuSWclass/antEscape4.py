testCase = int(input())

'''
1
6 2
.O&#@#
10 50
100 8
'''
def crushWall(ant, wolrd, crush):
    # print('***crushWall init***')
    for i in range(ant, ant-crush-1, -1):
        if wolrd[i] == '#':
            del wolrd[i]

    for i in range(ant, ant+crush, 1):
        if world[i] == '#':
            del world[i]

    ant = world.index('@')
    return ant, world

def fightMonster(atk_ant, hp_ant, atk_m, hp_m):
    # print('***fightMonster init***')
    flag = True
    while True:
        hp_m -= atk_ant
        # print(hp_ant, hp_m)
        if hp_m <= 0:
            break

        hp_ant -= atk_m
        # print(hp_ant, hp_m)
        if hp_ant <= 0:
            flag = False
            break

    return flag


for test in range(testCase):
    length, crush = map(int, input().split())
    world = list( input().strip().replace('.', ''))
    ant = world.index('@')
    atk_ant, hp_ant = map(int, input().split())
    atk_m, hp_m = map(int, input().split())

    if '#' in world and crush > 0:
        ant, world = crushWall(ant, world, crush)

    flag = True
    if ant != 0 and ant != length-1:
        if world[ant-1] == '&' or world[ant+1] == '&':
            flag = fightMonster(atk_ant, hp_ant, atk_m, hp_m)

    elif ant == 0:
        if world[ant+1] == '&':
            flag = fightMonster(atk_ant, hp_ant, atk_m, hp_m)

    elif ant == length-1:
        if world[ant-1] == '&':
            flag = fightMonster(atk_ant, hp_ant, atk_m, hp_m)

    if flag:
        print('HAHA!')
    else:
        print('HELP!')

