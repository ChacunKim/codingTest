testCase = int(input())
'''

'''
def crushWalls(ant, world, crush):
    for i in range(crush):
        if ant-1 >= 0 and world[ant-1] == '#':
            del world[ant-1]
            ant -= 1

        if ant+1 <= len(world) and world[ant+1] == '#':
            del world[ant+1]

    return ant, world

def fightMonster(atk_ant, hp_ant, atk_m, hp_m):
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


for test in range(testCase):
    length, crush = map(int, input().split())
    world = list( input().strip().replace('.', ''))
    ant = world.index('@')
    atk_ant, hp_ant = map(int, input().split())
    atk_m, hp_m = map(int, input().split())

    if '#' in world and crush > 0:
        ant, world = crushWalls(ant, world, crush)

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

